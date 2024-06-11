Geos Series Accessor
====================

.. currentmodule:: pgpd

.. autoclass:: GeosSeriesAccessor


Serialization
-------------
Serialization & Deserialization functionality.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosSeriesAccessor.to_geos
   GeosSeriesAccessor.to_geopandas
   GeosSeriesAccessor.to_wkt
   GeosSeriesAccessor.to_wkb

Geometry
--------
Methods from :doc:`Shapely Geometry Properties <shapely:properties>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosSeriesAccessor.get_coordinate_dimension
   GeosSeriesAccessor.get_dimensions
   GeosSeriesAccessor.get_exterior_ring
   GeosSeriesAccessor.get_geometry
   GeosSeriesAccessor.get_interior_ring
   GeosSeriesAccessor.get_num_coordinates
   GeosSeriesAccessor.get_num_geometries
   GeosSeriesAccessor.get_num_interior_rings
   GeosSeriesAccessor.get_num_points
   GeosSeriesAccessor.get_parts
   GeosSeriesAccessor.get_point
   GeosSeriesAccessor.get_precision
   GeosSeriesAccessor.get_rings
   GeosSeriesAccessor.get_srid
   GeosSeriesAccessor.get_type_id
   GeosSeriesAccessor.get_x
   GeosSeriesAccessor.get_y
   GeosSeriesAccessor.get_z
   GeosSeriesAccessor.force_2d
   GeosSeriesAccessor.force_3d
   GeosSeriesAccessor.set_precision
   GeosSeriesAccessor.set_srid


Geometry Creation
-----------------
Methods from :doc:`Shapely Geometry Creation <shapely:creation>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosSeriesAccessor.destroy_prepared
   GeosSeriesAccessor.prepare


Measurement
-----------
Methods from :doc:`Shapely Measurement <shapely:measurement>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.area
    GeosSeriesAccessor.bounds
    GeosSeriesAccessor.distance
    GeosSeriesAccessor.frechet_distance
    GeosSeriesAccessor.hausdorff_distance
    GeosSeriesAccessor.length
    GeosSeriesAccessor.minimum_bounding_radius
    GeosSeriesAccessor.minimum_clearance
    GeosSeriesAccessor.total_bounds


Predicates
----------
Methods from :doc:`Shapely Predicates <shapely:predicates>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.contains
    GeosSeriesAccessor.contains_properly
    GeosSeriesAccessor.covered_by
    GeosSeriesAccessor.covers
    GeosSeriesAccessor.crosses
    GeosSeriesAccessor.disjoint
    GeosSeriesAccessor.equals
    GeosSeriesAccessor.equals_exact
    GeosSeriesAccessor.has_z
    GeosSeriesAccessor.intersects
    GeosSeriesAccessor.is_ccw
    GeosSeriesAccessor.is_closed
    GeosSeriesAccessor.is_empty
    GeosSeriesAccessor.is_geometry
    GeosSeriesAccessor.is_missing
    GeosSeriesAccessor.is_prepared
    GeosSeriesAccessor.is_ring
    GeosSeriesAccessor.is_simple
    GeosSeriesAccessor.is_valid
    GeosSeriesAccessor.is_valid_input
    GeosSeriesAccessor.is_valid_reason
    GeosSeriesAccessor.overlaps
    GeosSeriesAccessor.relate
    GeosSeriesAccessor.relate_pattern
    GeosSeriesAccessor.touches
    GeosSeriesAccessor.within


Set Operations
--------------
Methods from :doc:`Shapely Set Operations <shapely:set_operations>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.coverage_union
    GeosSeriesAccessor.coverage_union_all
    GeosSeriesAccessor.difference
    GeosSeriesAccessor.intersection
    GeosSeriesAccessor.intersection_all
    GeosSeriesAccessor.symmetric_difference
    GeosSeriesAccessor.symmetric_difference_all
    GeosSeriesAccessor.union
    GeosSeriesAccessor.union_all


Constructive Operations
------------------------
Methods from :doc:`Shapely Constructive Operations <shapely:constructive>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.boundary
    GeosSeriesAccessor.buffer
    GeosSeriesAccessor.build_area
    GeosSeriesAccessor.centroid
    GeosSeriesAccessor.clip_by_rect
    GeosSeriesAccessor.convex_hull
    GeosSeriesAccessor.delaunay_triangles
    GeosSeriesAccessor.envelope
    GeosSeriesAccessor.extract_unique_points
    GeosSeriesAccessor.make_valid
    GeosSeriesAccessor.minimum_bounding_circle
    GeosSeriesAccessor.minimum_rotated_rectangle
    GeosSeriesAccessor.normalize
    GeosSeriesAccessor.offset_curve
    GeosSeriesAccessor.oriented_envelope
    GeosSeriesAccessor.point_on_surface
    GeosSeriesAccessor.polygonize
    GeosSeriesAccessor.reverse
    GeosSeriesAccessor.segmentize
    GeosSeriesAccessor.simplify
    GeosSeriesAccessor.snap
    GeosSeriesAccessor.voronoi_polygons


Linestring Operations
---------------------
Methods from :doc:`Shapely Linestring Operations <shapely:linear>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.line_interpolate_point
    GeosSeriesAccessor.line_locate_point
    GeosSeriesAccessor.line_merge
    GeosSeriesAccessor.shared_paths
    GeosSeriesAccessor.shortest_line


Coordinate Operations
---------------------
Methods from :doc:`Shapely Coordinate Operations <shapely:coordinates>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.transform
    GeosSeriesAccessor.count_coordinates
    GeosSeriesAccessor.get_coordinates_2d
    GeosSeriesAccessor.get_coordinates_3d
    GeosSeriesAccessor.set_coordinates


STRTree
-------
Methods from :doc:`Shapely STRTree <shapely:strtree>`.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

    GeosSeriesAccessor.STRtree


Custom
------
Custom methods to add more functionality.

.. autosummary::
   :toctree: generated
   :nosignatures:
   :template: base.rst

   GeosSeriesAccessor.affine
   GeosSeriesAccessor.rotate
   GeosSeriesAccessor.scale
   GeosSeriesAccessor.skew
   GeosSeriesAccessor.translate


.. include:: /links.rst
