Access
======



The PDC products may be accessed via web servives (simpler) or through their archived version in Zenodo.

Web Services Endpoint (Recommended):
-------------------------------------
The base URL is

https://geoserver.panalesis.org/geoserver/

.. list-table:: Available Layers
   :header-rows: 1
   :widths: 25 30 35 10

   * - Layer Name
     - Workspace
     - Full Layer Identifier
     - CRS
   * - **Crustal Thickness**
     - panalesis_atlas
     - ``panalesis_atlas:crustal_thickness``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:crustal_thickness_4326``
     - EPSG:4326
   * - **Hydrothermal Penetration**
     - panalesis_atlas
     - ``panalesis_atlas:hydrothermal_penetration``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:hydrothermal_penetration_4326``
     - EPSG:4326
   * - **Lithospheric Thickness**
     - panalesis_atlas
     - ``panalesis_atlas:lithospheric_thickness``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:lithospheric_thickness_4326``
     - EPSG:4326
   * - **Palaeogeography**
     - panalesis_atlas
     - ``panalesis_atlas:palaeogeography``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:palaeogeography_4326``
     - EPSG:4326
   * - **Seafloor Ages**
     - panalesis_atlas
     - ``panalesis_atlas:seafloor_ages``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:seafloor_ages_4326``
     - EPSG:4326
   * - **Flow Direction**
     - panalesis_atlas
     - ``panalesis_atlas:flow_dir``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:flow_dir_4326``
     - EPSG:4326
   * - **Flow Accumulation**
     - panalesis_atlas
     - ``panalesis_atlas:flow_acc``
     - ESRI:54034
   * -
     - panalesis_atlas_epsg_4326
     - ``panalesis_atlas_epsg_4326:flow_acc_4326``
     - EPSG:4326

The layers are loaded as ImageMosaics, with time enabled. In order to accommodate the unusual geological time scales,
we have tweaked the time dimensions to be compatible with ISO 8601 format.

The geological age (in Myr) is added to the year 2000 in the date property. For instance:

* ``000 Myr (present-day)``: ``TIME=2000-01-01T00:00:00.000Z``
* ``-250 Myr``: ``TIME=2250-01-01T00:00:00.000Z``
* ``-545 Myr``: ``TIME=2545-01-01T00:00:00.00``

Zenodo (Alternative):
----------------------

#. **Palaeogeography:** Franziskakis, F., Vérard, C., Castelltort, S., & Giuliani, G. (2025). Global Quantified Palaeogeographic Maps and Associated Sea-level Variations for the Phanerozoic using the PANALESIS Model [Data set]. *Zenodo*. https://doi.org/10.5281/zenodo.15396265
#. **Atlas**: Franziskakis, F., Werner, N., Vérard, C., Castelltort, S., & Giuliani, G. (2026). A Phanerozoic Atlas of Earth's Atmosphere, Surface, and Interior Derived from the PANALESIS Plate Tectonic Model (v1.0) [Data set]. *Zenodo*. https://doi.org/10.5281/zenodo.19134591

Metadata Catalog
----------------
Every product is documented with standard metadata (ISO 19115). The catalog is supported by GeoNetwork and can be
accessed `here <https://geonetwork.panalesis.org/geonetwork>`_.

A SpatioTemporal Assets Catalog (STAC) listing every item available for every product (one collection per product) is
available in the `stac folder <https://github.com/florianfranz/palaeo-data-cube/tree/main/stac>`_.

