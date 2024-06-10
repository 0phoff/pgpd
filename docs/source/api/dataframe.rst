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

   GeosDataFrameAccessor.to_geos
   GeosDataFrameAccessor.to_geopandas
   GeosSeriesAccessor.to_shapely
   GeosSeriesAccessor.to_wkt
   GeosSeriesAccessor.to_wkb

Geometry
--------
Methods from :doc:`Shapely Geometry Properties <shapely:properties>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosDataFrameAccessor.get_coordinate_dimension
   GeosDataFrameAccessor.get_dimensions
   GeosDataFrameAccessor.get_exterior_ring
   GeosDataFrameAccessor.get_geometry
   GeosDataFrameAccessor.get_interior_ring
   GeosDataFrameAccessor.get_num_coordinates
   GeosDataFrameAccessor.get_num_geometries
   GeosDataFrameAccessor.get_num_interior_rings
   GeosDataFrameAccessor.get_num_points
   GeosDataFrameAccessor.get_point
   GeosDataFrameAccessor.get_precision
   GeosDataFrameAccessor.get_srid
   GeosDataFrameAccessor.get_type_id
   GeosDataFrameAccessor.get_x
   GeosDataFrameAccessor.get_y
   GeosDataFrameAccessor.get_z
   GeosDataFrameAccessor.force_2d
   GeosDataFrameAccessor.force_3d
   GeosDataFrameAccessor.set_precision
   GeosDataFrameAccessor.set_srid


Geometry Creation
-----------------
Methods from :doc:`Shapely Geometry Creation <shapely:creation>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosDataFrameAccessor.destroy_prepared
   GeosDataFrameAccessor.prepare


Measurement
-----------
Methods from :doc:`Shapely Measurement <shapely:measurement>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.area
    GeosDataFrameAccessor.length
    GeosDataFrameAccessor.minimum_bounding_radius
    GeosDataFrameAccessor.minimum_clearance
    GeosDataFrameAccessor.total_bounds


Predicates
----------
Methods from :doc:`Shapely Predicates <shapely:predicates>`.

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
Methods from :doc:`Shapely Constructive Operations <shapely:constructive>`.

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
    GeosDataFrameAccessor.minimum_bounding_circle
    GeosDataFrameAccessor.minimum_rotated_rectangle
    GeosDataFrameAccessor.normalize
    GeosDataFrameAccessor.offset_curve
    GeosDataFrameAccessor.oriented_envelope
    GeosDataFrameAccessor.point_on_surface
    GeosDataFrameAccessor.reverse
    GeosDataFrameAccessor.simplify
    GeosDataFrameAccessor.snap
    GeosDataFrameAccessor.voronoi_polygons


Linestring Operations
---------------------
Methods from :doc:`Shapely Linestring Operations <shapely:linear>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.line_interpolate_point
    GeosDataFrameAccessor.line_locate_point
    GeosDataFrameAccessor.line_merge


Coordinate Operations
---------------------
Methods from :doc:`Shapely Coordinate Operations <shapely:coordinates>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosDataFrameAccessor.transform
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


.. include:: /links.rst
