#
# Shapely - PyGEOS Conversion
#
import contextlib
import warnings
from distutils.version import LooseVersion

import pygeos

try:
    import shapely
    from shapely.geometry.base import BaseGeometry as ShapelyGeometry
except ImportError:
    shapely = None
    ShapelyGeometry = None

__all__ = ['shapely', 'ShapelyGeometry', 'PYGEOS_SHAPELY_COMPAT', 'IGNORE_SHAPELY2_WARNINGS']


PYGEOS_SHAPELY_COMPAT = None


@contextlib.contextmanager
def IGNORE_SHAPELY2_WARNINGS():
    yield



if shapely is not None:
    # -------------------------------------------------------------------------
    # Geos Compatibility
    # -------------------------------------------------------------------------
    from shapely.geos import geos_version_string as shapely_geos_version
    from pygeos import geos_capi_version_string as pygeos_geos_version

    # shapely has something like: "3.6.2-CAPI-1.10.2 4d2925d6"
    # pygeos has something like: "3.6.2-CAPI-1.10.2"
    if not shapely_geos_version.startswith(pygeos_geos_version):
        warnings.warn(
            "The Shapely GEOS version ({}) is incompatible with the GEOS "
            "version PyGEOS was compiled with ({}). Conversions between both "
            "will be slow.".format(
                shapely_geos_version, pygeos_geos_version
            )
        )
        PYGEOS_SHAPELY_COMPAT = False
    else:
        PYGEOS_SHAPELY_COMPAT = True

    # -------------------------------------------------------------------------
    # Shapely warnings
    # -------------------------------------------------------------------------
    if str(shapely.__version__) >= LooseVersion("2.0"):
        try:
            from shapely.errors import ShapelyDeprecationWarning as shapely_warning

            @contextlib.contextmanager
            def IGNORE_SHAPELY2_WARNINGS():
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", "Iteration|The array interface|__len__", shapely_warning)
                    yield
        except ImportError:
            pass
