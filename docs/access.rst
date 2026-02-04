Access
======



The PDC products may be accessed via web servives (simpler) or through their archived version in Zenodo.

Web Services Endpoint (Recommended):
-------------------------------------
The base URL is

https://geoserver.panalesis.org/geoserver/

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Layer Name
     - Workspace
     - Full Layer Identifier
   * - Crustal Thickness
     - panalesis_atlas
     - ``panalesis_atlas:crustal_thickness``
   * - Hydrothermal Penetration
     - panalesis_atlas
     - ``panalesis_atlas:hydrothermal_penetration``
   * - Lithospheric Thickness
     - panalesis_atlas
     - ``panalesis_atlas:lithospheric_thickness``
   * - Palaeogeography
     - panalesis_atlas
     - ``panalesis_atlas:palaeogeography``
   * - Seafloor Ages
     - panalesis_atlas
     - ``panalesis_atlas:seafloor_ages``
   * - Flow Direction
     - panalesis_atlas
     - ``panalesis_atlas:flow_dir``
   * - Flow Accumulation
     - panalesis_atlas
     - ``panalesis_atlas:flow_acc``

The layers are loaded as ImageMosaics, with time enabled. In order to accommodate the unusual geological time scales,
we have tweaked the time dimensions to be compatible with ISO 8601 format.

The geological age (in Myr) is added to the year 2000 in the date property. For instance:

* ``000 Myr (present-day)``: ``TIME=2000-01-01T00:00:00.000Z``
* ``-250 Myr``: ``TIME=2250-01-01T00:00:00.000Z``
* ``-545 Myr``: ``TIME=2545-01-01T00:00:00.00``

Zenodo (Alternative):
----------------------
Currently, only palaeogeographic maps are stored on Zenodo. Other products will soon be added.

#. **Palaeogeography:** Franziskakis, F., Vérard, C., Castelltort, S., & Giuliani, G. (2025). Global Quantified Palaeogeographic Maps and Associated Sea-level Variations for the Phanerozoic using the PANALESIS Model [Data set]. *Zenodo*. https://doi.org/10.5281/zenodo.15396265

Metadata Catalog
----------------
Every product is documented with standard metadata (ISO 19115). The catalog is supported by GeoNetwork and can be
accessed `here <https://geonetwork.panalesis.org/geonetwork>`_.

A SpatioTemporal Assets Catalog (STAC) listing every item available for every product (one collection per product) is
available in the `stac folder <https://github.com/florianfranz/palaeo-data-cube/tree/main/stac>`_.

