#
# PyGEOS ExtensionDType & ExtensionArray
#
import numbers
from collections.abc import Iterable
import numpy as np
import pandas as pd
import pygeos
from pandas.api.extensions import ExtensionArray, ExtensionDtype, register_extension_dtype
from ._shapely import shapely, ShapelyGeometry, PYGEOS_SHAPELY_COMPAT, IGNORE_SHAPELY2_WARNINGS

__all__ = ['GeosDtype', 'GeosArray']


class GeosDtype(ExtensionDtype):
    type = pygeos.lib.Geometry
    name = 'geos'
    na_value = pd.NA

    @classmethod
    def construct_from_string(cls, string):
        if string == cls.name:
            return cls()
        else:
            raise TypeError(
                "Cannot construct a '{}' from '{}'".format(cls.__name__, string)
            )

    @classmethod
    def construct_array_type(cls):
        return GeosArray


register_extension_dtype(GeosDtype)


def _pygeos_to_shapely(geom):
    if geom is None:
        return None

    if PYGEOS_SHAPELY_COMPAT:
        geom = shapely.geos.lgeos.GEOSGeom_clone(geom._ptr)
        return shapely.geometry.base.geom_factory(geom)

    # fallback going through WKB
    if pygeos.is_empty(geom) and pygeos.get_type_id(geom) == 0:
        # empty point does not roundtrip through WKB
        return shapely.wkt.loads("POINT EMPTY")
    else:
        return shapely.wkb.loads(pygeos.to_wkb(geom))


class GeosArray(ExtensionArray):
    _dtype = GeosDtype()
    ndim = 1

    # -------------------------------------------------------------------------
    # (De-)Serialization
    # -------------------------------------------------------------------------

    def __init__(self, data):
        if isinstance(data, self.__class__):
            self.data = data.data
        elif data is None or isinstance(data, self._dtype.type):
            self.data = np.array((data,))
        elif isinstance(data, Iterable) and (data[0] is None or isinstance(data[0], self._dtype.type)):
            self.data = np.array(data)
        else:
            raise ValueError(f'Data should be an iterable of {self._dtype.type}')

        self.data[pd.isnull(self.data)] = None

    @classmethod
    def from_shapely(cls, data, **kwargs):
        data = pygeos.io.from_shapely(data, **kwargs)
        return cls(data)

    @classmethod
    def from_wkb(cls, data, **kwargs):
        data = pygeos.io.from_wkb(data, **kwargs)
        return cls(data)

    @classmethod
    def from_wkt(cls, data, **kwargs):
        data = pygeos.io.from_wkt(data, **kwargs)
        return cls(data)

    def to_shapely(self):
        out = np.empty(len(self.data), dtype=object)
        with IGNORE_SHAPELY2_WARNINGS():
            out[:] = [_pygeos_to_shapely(g) for g in self.data]
        return out

    def to_wkb(self, **kwargs):
        return pygeos.io.to_wkb(self.data, **kwargs)

    def to_wkt(self, **kwargs):
        return pygeos.io.to_wkt(self.data, **kwargs)

    # -------------------------------------------------------------------------
    # ExtensionArray Specific
    # -------------------------------------------------------------------------

    @classmethod
    def _from_sequence(cls, scalars, dtype=None, copy=False):
        if isinstance(scalars, (str, bytes)) or not isinstance(scalars, Iterable):
            scalars = (scalars,)

        values = np.array(scalars)
        if copy:
            values = values.copy()

        if isinstance(values[0], str):
            return cls.from_wkt(values)
        elif isinstance(values[0], bytes):
            return cls.from_wkb(values)
        elif ShapelyGeometry is not None and isinstance(values[0], ShapelyGeometry):
            return cls.from_shapely(values)

        return cls(values)

    def _values_for_factorize(self):
        return self.data, None

    @classmethod
    def _from_factorized(cls, values, original):
        return cls(values)

    def __getitem__(self, key):
        if isinstance(key, numbers.Integral):
            return self.data[key]

        key = pd.api.indexers.check_array_indexer(self, key)
        if isinstance(key, (Iterable, slice)):
            return GeosArray(self.data[key])
        else:
            raise TypeError("Index type not supported", key)

    def __setitem__(self, key, value):
        key = pd.api.indexers.check_array_indexer(self, key)


    def __len__(self):
        return self.data.shape[0]

    def __eq__(self, other):
        if isinstance(other, (pd.Series, pd.Index, pd.DataFrame)):
            return NotImplemented

        if isinstance(other, self.__class__):
            return self.data == other.data

        return self.data == other

    @property
    def dtype(self):
        return self._dtype

    @property
    def nbytes(self):
        return self.data.nbytes

    def isna(self):
        return pygeos.is_missing(self.data)

    def take(self, indices, allow_fill=False, fill_value=None):
        from pandas.core.algorithms import take

        if allow_fill:
            if fill_value is None or pd.isna(fill_value):
                fill_value = None
            elif not isinstance(fill_value, self._dtype.type):
                raise TypeError("Provide geometry or None as fill value")

        result = take(self.data, indices, allow_fill=allow_fill, fill_value=fill_value)

        if allow_fill and fill_value is None:
            result[pd.isna(result)] = None
        
        return self.__class__(result)

    def copy(self, order='C'):
        return GeosArray(self.data.copy(order))

    def _concat_same_type(self, to_concat):
        data = np.concatenate([c.data for c in to_concat])
        return self.__class__(data)

    def _values_for_argsort(self):
        raise TypeError("geometries are not orderable")

    # -------------------------------------------------------------------------
    # NumPy Specific
    # -------------------------------------------------------------------------

    @property
    def size(self):
        return self.data.size

    @property
    def shape(self):
        return self.data.shape

    def __array__(self, dtype=None):
        return self.data
