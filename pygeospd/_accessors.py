#
# Geo Accessor for a DataFrame
#
import pandas as pd
from ._array import GeosArray
from ._delegated import *

try:
    import geopandas as gpd
except ImportError:
    gpd = None


__all__ = ['GeosSeriesAccessor', 'GeosDataFrameAccessor']


@pd.api.extensions.register_series_accessor("geos")
class GeosSeriesAccessor:
    def __init__(self, obj):
        if gpd is not None and isinstance(obj, gpd.GeoSeries):
            obj = pd.Series(GeosArray(obj.array.data))
        elif (pd.api.types.pandas_dtype('geos') != obj.dtype):
            raise AttributeError(f'Cannot use "geos" accessor on objects of dtype "{obj.dtype}"')
        self._obj = obj

    def to_geopandas(self, crs=None, copy=False):
        """
        Convert a geos Series into a :class:`geopandas.GeoSeries`.

        Args:
            crs (any, optional): CRS to use with GeoPandas, check the docs for more information; Default **None** 
            copy (bool, optional): Whether to copy the data or return a wrapper around the same data; Default **False**

        Returns:
            geopandas.GeoSeries: The geopandas series.

        Raises:
            ImportError: Geopandas is not installed.
            AttributeError: Series is not of geos dtype.
        """
        if gpd is None:
            raise ImportError('Geopandas is required for this function')

        if isinstance(self._obj, gpd.GeoSeries):
            s = self._obj
        else:
            s = gpd.GeoSeries(self._obj.astype(object), crs=crs)

        if copy:
            return s.copy()
        else:
            return s

    def from_geopandas(self, copy=False):
        """
        Transform a :class:`geopandas.GeoSeries` into a regular Series with a geos dtype.

        Args:
            copy (bool, optional): Whether to copy the data or return a wrapper around the same data; Default **False**

        Returns:
            pd.Series: Series with a geos dtype.
        """
        if copy:
            return self._obj.copy()
        else:
            return self._obj

    # -------------------------------------------------------------------------
    # Geometry Creation
    # -------------------------------------------------------------------------
    destroy_prepared = get_ReturnMethodUnary('creation.destroy_prepared')
    prepare = get_ReturnMethodUnary('creation.prepare')

    # -------------------------------------------------------------------------
    # Measurement
    # -------------------------------------------------------------------------
    area = get_IndexedSeriesProperty('measurement.area')
    bounds = get_IndexedDataFrameProperty('measurement.bounds', ['xmin', 'ymin', 'xmax', 'ymax'])
    distance = get_MethodBinary('measurement.distance')
    frechet_distance = get_MethodBinary('measurement.frechet_distance')
    hausdorff_distance = get_MethodBinary('measurement.hausdorff_distance')
    length = get_IndexedSeriesProperty('measurement.length')
    minimum_clearance = get_IndexedSeriesProperty('measurement.minimum_clearance')
    total_bounds = get_SeriesProperty('measurement.total_bounds', ['xmin', 'ymin', 'xmax', 'ymax'])

    # -------------------------------------------------------------------------
    # Predicates
    # -------------------------------------------------------------------------
    contains = get_MethodBinary('predicates.contains')
    contains_properly = get_MethodBinary('predicates.contains_properly')
    covered_by = get_MethodBinary('predicates.covered_by')
    covers = get_MethodBinary('predicates.covers')
    crosses = get_MethodBinary('predicates.crosses')
    disjoint = get_MethodBinary('predicates.disjoint')
    equals = get_MethodBinary('predicates.equals')
    equals_exact = get_MethodBinary('predicates.equals_exact')
    has_z = get_IndexedSeriesProperty('predicates.has_z')
    intersects = get_MethodBinary('predicates.intersects')
    is_ccw = get_IndexedSeriesProperty('predicates.is_ccw')
    is_closed = get_IndexedSeriesProperty('predicates.is_closed')
    is_empty = get_IndexedSeriesProperty('predicates.is_empty')
    is_geometry = get_IndexedSeriesProperty('predicates.is_geometry')
    is_missing = get_IndexedSeriesProperty('predicates.is_missing')
    is_prepared = get_IndexedSeriesProperty('predicates.is_prepared')
    is_ring = get_IndexedSeriesProperty('predicates.is_ring')
    is_simple = get_IndexedSeriesProperty('predicates.is_simple')
    is_valid = get_IndexedSeriesProperty('predicates.is_valid')
    is_valid_input = get_IndexedSeriesProperty('predicates.is_valid_input')
    is_valid_reason = get_IndexedSeriesProperty('predicates.is_valid_reason')
    overlaps = get_MethodBinary('predicates.overlaps')
    relate = get_MethodBinary('predicates.relate')
    relate_pattern = get_MethodBinary('predicates.relate_pattern')
    touches = get_MethodBinary('predicates.touches')
    within = get_MethodBinary('predicates.within')

    # -------------------------------------------------------------------------
    # Set operations
    # -------------------------------------------------------------------------
    coverage_union = get_MethodBinary('set_operations.coverage_union', geos=True)
    coverage_union_all = get_ReturnMethodUnary('set_operations.coverage_union_all')
    difference = get_MethodBinary('set_operations.difference', geos=True)
    intersection = get_MethodBinary('set_operations.intersection', geos=True)
    intersection_all = get_ReturnMethodUnary('set_operations.intersection_all')
    symmetric_difference = get_MethodBinary('set_operations.symmetric_difference', geos=True)
    symmetric_difference_all = get_ReturnMethodUnary('set_operations.symmetric_difference_all')
    union = get_MethodBinary('set_operations.union', geos=True)
    union_all = get_ReturnMethodUnary('set_operations.union_all')

    # -------------------------------------------------------------------------
    # Constructive operations
    # -------------------------------------------------------------------------
    boundary = get_IndexedSeriesProperty('constructive.boundary', geos=True)
    buffer = get_IndexedSeriesMethodUnary('constructive.buffer', geos=True)
    # build_area = 
    centroid = get_IndexedSeriesProperty('constructive.centroid', geos=True)
    clip_by_rect = get_IndexedSeriesMethodUnary('constructive.clip_by_rect', geos=True)
    convex_hull = get_IndexedSeriesProperty('constructive.convex_hull', geos=True)
    delaunay_triangles = get_IndexedSeriesMethodUnary('constructive.delaunay_triangles', geos=True)
    envelope = get_IndexedSeriesProperty('constructive.envelope', geos=True)
    extract_unique_points = get_IndexedSeriesProperty('constructive.extract_unique_points', geos=True)
    make_valid = get_IndexedSeriesProperty('constructive.make_valid', geos=True)
    normalize = get_IndexedSeriesProperty('constructive.normalize', geos=True)
    offset_curve = get_IndexedSeriesMethodUnary('constructive.offset_curve', geos=True)
    point_on_surface = get_IndexedSeriesProperty('constructive.point_on_surface', geos=True)
    polygonize = get_ReturnMethodUnary('constructive.polygonize')
    reverse = get_IndexedSeriesProperty('constructive.reverse', geos=True)
    # segmentize = 
    simplify = get_IndexedSeriesProperty('constructive.simplify', geos=True)
    snap = get_IndexedSeriesMethodUnary('constructive.snap', geos=True)
    voronoi_polygons = get_IndexedSeriesMethodUnary('constructive.voronoi_polygons', geos=True)

    # -------------------------------------------------------------------------
    # Linestring operations
    # -------------------------------------------------------------------------
    line_interpolate_point = get_IndexedSeriesMethodUnary('linear.line_interpolate_point', geos=True)
    line_locate_point = get_IndexedSeriesMethodUnary('linear.line_locate_point', geos=True)
    line_merge = get_IndexedSeriesProperty('linear.line_merge', geos=True)
    shared_paths = get_MethodBinary('linear.shared_paths', geos=True)

    # -------------------------------------------------------------------------
    # Coordinate operations
    # -------------------------------------------------------------------------
    apply = get_IndexedSeriesMethodUnary('coordinates.apply', geos=True)
    count_coordinates = get_IndexedSeriesProperty('coordinates.count_coordinates')
    get_coordinates = get_SeriesMethodUnary('coordinates.get_coordinates')
    set_coordinates = get_IndexedSeriesMethodUnary('coordinates.set_coordinates', geos=True)

    # -------------------------------------------------------------------------
    # STRTree
    # -------------------------------------------------------------------------
    STRTree = get_ReturnMethodUnary('strtree.STRtree')


@pd.api.extensions.register_dataframe_accessor("geos")
class GeosDataFrameAccessor:
    def __init__(self, obj):
        if gpd is not None and isinstance(obj, gpd.GeoDataFrame):
            geometry = obj._geometry_column_name
            obj = pd.DataFrame(obj).copy()
            obj[geometry] = GeosArray(obj[geometry].array.data)
        elif (obj.dtypes != 'geos').all():
            raise AttributeError('Must have at least one "geos" dtype column')
        self._obj = obj

    def to_geopandas(self, geometry=None, crs=None):
        """
        Transform a pandas DataFrame with (at least) a "geos" dtype column to a :class:`geopandas.GeoDataFrame`.

        Args:
            geometry (string, optional): Name of the column to use as geometry; Default **Infer if there is only one geos column**
            crs (any, optional): CRS to use with GeoPandas, check the docs for more information; Default **None** 

        Returns:
            geopandas.GeoDataFrame: The geopandas dataframe.

        Raises:
            ImportError: Geopandas is not installed.
            AttributeError: There are no geos dtype columns in the dataframe.
            TypeError: "geometry" column is not of geos dtype.
            ValueError: No "geometry" was passed, but there are multiple "geos" column so we cannot automatically infer.

        Note:
            This function always returns a copy of the original data.
        """
        if gpd is None:
            raise ImportError('Geopandas is required for this function')
        if isinstance(self._obj, gpd.GeoDataFrame):
            return self._obj.copy()

        geos_columns = self._obj.dtypes[self._obj.dtypes == 'geos'].index
        if geometry is not None and geometry not in geos_columns:
            raise TypeError(f'Column "{column}" should be of "geos" type')
        elif geometry is None:
            if len(geos_columns) != 1:
                raise ValueError(f'There are multiple columns of "geos", please specify which one to use as geometry')
            geometry = geos_columns[0]

        df = self._obj.copy()
        df[geometry] = df[geometry].astype(object)
        return gpd.GeoDataFrame(df, geometry=geometry, crs=crs)

    def from_geopandas(self):
        """
        Transform a :class:`geopandas.GeoDataFrame` into a regular DataFrame with a geos column.

        Returns:
            pd.DataFrame: DataFrame where the geometry column is transformed into a geos dtype.

        Note:
            This function always returns a copy of the original data.
        """
        return self._obj.copy()


# Set convenience properties and methods on DataFrame accessor
# They simply call the Series accessor equivalent for each geos column and group the result
for name in dir(GeosSeriesAccessor):
    if name.startswith('__'):
        continue

    item = getattr(GeosSeriesAccessor, name)
    if isinstance(item, property) and hasattr(item.fget, '__DataFrameExpand__'):
        setattr(GeosDataFrameAccessor, name, get_DataFrameExpandedProperty(name, item.fget.__DataFrameExpand__))
    elif callable(item) and hasattr(item, '__DataFrameExpand__'):
        setattr(GeosDataFrameAccessor, name, get_DataFrameExpandedMethodUnary(name, item.__DataFrameExpand__))
