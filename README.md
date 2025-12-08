# Palaeo Data Cube (PDC)

## Overview
The Palaeo Data Cube (PDC) provides global maps of the Earth in deep-time (currently of the last 545 million years, in 44 steps). It is inspired by the present-day Earth Observations (EO) Data Cubes, and provides acess to data products in high-resolution of the Earth system long-term evolution.

![PAN_ages.svg](images%2FPAN_ages.svg)
## Data products

The PDC provides access to global maps depicting various aspects of the Earth over the Phanerozoic, derived from the PANALESIS plate tectonic model. Layers are available for:

1. Palaeogeography: Topographic maps with sea-level corrections, calculated based on the global oceanic basin size (assuming constant oceanic volume through time). Our reconstructions do not have flat seafloor.
2. Crustal thickness
3. Seafloor ages
4. Lithospheric thickness
5. Maximum hydrothermal penetration depth
6. Flow direction
7. Flow accumulation

More products from climate simulations will be added in the near future.

![PDC.png](images%2FPDC.png)

Maps are available for every reconstruction mentionned above, share the same projection, resolution and extent. The specifications are the following:

| Property    | Value                                             |
|-------------|---------------------------------------------------|
| Projection  | [ESRI:54034](https://epsg.io/54034)               |
| Resolution  | 10 × 10 km                                        |
| Extent      | -20037508.34 -6363885.33, 20037508.34, 6363885.33 |


## Architecture

The PDC is based on open source solutions for serving, describing, searching and archiving the data prodcucts. They are the following:

| Component                      | Technology    | Purpose                                                        |
|-------------------------------|--------------|----------------------------------------------------------------|
| **Data Server**              | GeoServer    | Serves geospatial data via OGC web map services (WMS)          |
| **Metadata Catalog (static)**| GeoNetwork   | Stores and publishes ISO/INSPIRE metadata records              |
| **Metadata Catalog (dynamic)**| STAC         | Provides dynamic, API-based metadata for spatiotemporal assets |
| **Data Archive**             | Zenodo       | Long-term storage, DOI assignement, version management         |


## Data Access

The PDC products may be accessed via WMS (simpler) or through their archived version in Zenodo.

**WMS Endpoint:** `https://geoserver.panalesis.org/geoserver/`

| Layer Name | Workspace | Full Layer Identifier |
|------------|-----------|----------------------|
| Crustal Thickness | panalesis_atlas | `panalesis_atlas:crustal_thickness` |
| Hydrothermal Penetration | panalesis_atlas | `panalesis_atlas:hydrothermal_penetration` |
| Lithospheric Thickness | panalesis_atlas | `panalesis_atlas:lithospheric_thickness` |
| Palaeogeography | panalesis_atlas | `panalesis_atlas:palaeogeography` |
| Seafloor Ages | panalesis_atlas | `panalesis_atlas:seafloor_ages` |

The layers are loaded as ImageMosaics, with time enabled. In order to accomodate the unusual geological times scales, we have tweaked the time dimensions to be compatible with ISO 8601 format. 

The geological age (in Myr) is added to the year 2000 in the date property. For instance:

`2250-01-01T00:00:00.000Z` will retrieve the map at -250 Myr (Permo-Triassic boundary)


**Zenodo:**
1. Palaeogeography:  Franziskakis, F., Vérard, C., Castelltort, S., & Giuliani, G. (2025). Global Quantified Palaeogeographic Maps and Associated Sea-level Variations for the Phanerozoic using the PANALESIS Model [Data set]. Zenodo. https://doi.org/10.5281/zenodo.15396265


## Contributors:

**Florian Franziskakis**  
*florian.franziskakis@unige.ch*  
enviroSPACE group, Institute for Environmental Sciences, University of Geneva

**Christian Vérard**  
Earth Surface Dynamics group, Department of Earth Sciences, University of Geneva

**Grégory Giuliani**  
enviroSPACE group, Institute for Environmental Sciences, University of Geneva

## License

This repository is licensed under the MIT license. 
You can view the full license text in the [LICENSE](./LICENSE).

## Funding

We acknowledge financial support from the Swiss National Science Foundation (SNSF) under [Sinergia grant #213539](https://data.snf.ch/grants/grant/213539): _Long-term 
evolution of the Earth from the base of the mantle to the top of the atmosphere: Understanding the mechanisms leading to ‘greenhouse’ and ‘icehouse’ regimes_.

This project is supported by an Open Research Data (ORD) grant from the University of Geneva