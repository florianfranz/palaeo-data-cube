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

![Full_PDC.png](images%2FFull_PDC.png)
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
| **STAC Browser**             | In development | Web-based interface for browsing and searching STAC catalog   |
| **Data Archive**             | Zenodo       | Long-term storage, DOI assignement, version management         |

## Data Access

The PDC products may be accessed via WMS (simpler) or through their archived version in Zenodo.

**WMS Endpoint (Recommended):** `https://geoserver.panalesis.org/geoserver/`

| Layer Name               | Workspace | Full Layer Identifier                      |
|--------------------------|-----------|--------------------------------------------|
| Crustal Thickness        | panalesis_atlas | `panalesis_atlas:crustal_thickness`        |
| Hydrothermal Penetration | panalesis_atlas | `panalesis_atlas:hydrothermal_penetration` |
| Lithospheric Thickness   | panalesis_atlas | `panalesis_atlas:lithospheric_thickness`   |
| Palaeogeography          | panalesis_atlas | `panalesis_atlas:palaeogeography`          |
| Seafloor Ages            | panalesis_atlas | `panalesis_atlas:seafloor_ages`            |
| Flow Direction           | panalesis_atlas | `panalesis_atlas:flow_dir`                 |
| Flow Accumulation        | panalesis_atlas | `panalesis_atlas:flow_acc`                 |

The layers are loaded as ImageMosaics, with time enabled. In order to accomodate the unusual geological times scales, we have tweaked the time dimensions to be compatible with ISO 8601 format. 

The geological age (in Myr) is added to the year 2000 in the date property. For instance:

- `000 Myr (present-day)` : `TIME=2000-01-01T00:00:00.000Z`
- `-250 Myr` : `TIME=2250-01-01T00:00:00.000Z`
- `-545 Myr` : `TIME=2545-01-01T00:00:00.00`

**Zenodo (Alternative):**

Currently, only palaeogeographic maps are stored on Zenodo. Other products will soon be added.
1. Palaeogeography:  Franziskakis, F., Vérard, C., Castelltort, S., & Giuliani, G. (2025). Global Quantified Palaeogeographic Maps and Associated Sea-level Variations for the Phanerozoic using the PANALESIS Model [Data set]. Zenodo. https://doi.org/10.5281/zenodo.15396265


## References

**PANALESIS Plate Tectonic Model**:

* Vérard, C., Hochard, C., Baumgartner, P. O., Stampfli, G. M., & Liu, M. (2015). 3D palaeogeographic reconstructions of the Phanerozoic versus sea-level and Sr-ratio variations. Journal of Palaeogeography, 4(1), Article 1. https://doi.org/10.3724/SP.J.1261.2015.00068
* Vérard, C. (2019). Panalesis: Towards global synthetic palaeogeographies using integration and coupling of manifold models. Geological Magazine, 156(2), Article 2. https://doi.org/10.1017/S0016756817001042
* Vérard, C. (2021). 888–444 Ma Global Plate Tectonic Reconstruction With Emphasis on the Formation of Gondwana. Frontiers in Earth Science, 9. https://www.frontiersin.org/articles/10.3389/feart.2021.666153

**EO Data Cubes**:

* Giuliani, G., Camara, G., Killough, B., & Minchin, S. (2019). Earth Observation Open Science: Enhancing Reproducible Science Using Data Cubes. Data, 4(4), 147. https://doi.org/10.3390/data4040147

**PDC Products & Applications:**

* Franziskakis, F., Vérard, C., Castelltort, S., & Giuliani, G. (2025). Comparing 545 Million Years of Sea-Level Change: New Insights from the TopoChronia QGIS Plugin. The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, XLVIII-4-W13-2025, 111–118. ISPRS ICWG IV/III/II. https://doi.org/10.5194/isprs-archives-XLVIII-4-W13-2025-111-2025


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