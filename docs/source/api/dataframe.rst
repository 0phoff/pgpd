Geos DataFrame Accessor
=======================

.. currentmodule:: pgpd

.. autoclass:: GeosDataFrameAccessor


Serialization
-------------
Serialization & Deserialization functionality.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosDataFrameAccessor.from_geopandas
   GeosDataFrameAccessor.to_geopandas


Measurement
-----------
Methods from :doc:`PyGEOS Measurement <pygeos:measurement>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.area
    GeosDataFrameAccessor.length
    GeosDataFrameAccessor.minimum_clearance
    GeosDataFrameAccessor.total_bounds


Predicates
----------
Methods from :doc:`PyGEOS Predicates <pygeos:predicates>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.has_z
    GeosDataFrameAccessor.is_ccw
    GeosDataFrameAccessor.is_closed
    GeosDataFrameAccessor.is_empty
    GeosDataFrameAccessor.is_geometry
    GeosDataFrameAccessor.is_missing
    GeosDataFrameAccessor.is_prepared
    GeosDataFrameAccessor.is_ring
    GeosDataFrameAccessor.is_simple
    GeosDataFrameAccessor.is_valid
    GeosDataFrameAccessor.is_valid_input
    GeosDataFrameAccessor.is_valid_reason


Constructive Operations
------------------------
Methods from :doc:`PyGEOS Constructive Operations <pygeos:constructive>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.boundary
    GeosDataFrameAccessor.buffer
    GeosDataFrameAccessor.centroid
    GeosDataFrameAccessor.clip_by_rect
    GeosDataFrameAccessor.convex_hull
    GeosDataFrameAccessor.delaunay_triangles
    GeosDataFrameAccessor.envelope
    GeosDataFrameAccessor.extract_unique_points
    GeosDataFrameAccessor.make_valid
    GeosDataFrameAccessor.normalize
    GeosDataFrameAccessor.offset_curve
    GeosDataFrameAccessor.point_on_surface
    GeosDataFrameAccessor.reverse
    GeosDataFrameAccessor.simplify
    GeosDataFrameAccessor.snap
    GeosDataFrameAccessor.voronoi_polygons


Linestring Operations
---------------------
Methods from :doc:`PyGEOS Linestring Operations <pygeos:linear>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.line_interpolate_point
    GeosDataFrameAccessor.line_locate_point
    GeosDataFrameAccessor.line_merge


Coordinate Operations
---------------------
Methods from :doc:`PyGEOS Coordinate Operations <pygeos:coordinates>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.apply
    GeosDataFrameAccessor.count_coordinates
    GeosDataFrameAccessor.set_coordinates


Custom
------
Custom methods to add more functionality.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosDataFrameAccessor.affine
   GeosDataFrameAccessor.rotate
   GeosDataFrameAccessor.scale
   GeosDataFrameAccessor.skew
   GeosDataFrameAccessor.translate
   GeosDataFrameAccessor.apply_shapely


.. include:: /links.rst
