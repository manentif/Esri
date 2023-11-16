ARG arcgis_version="2.2.0"
FROM ghcr.io/esri/arcgis-python-api-notebook:${arcgis_version}

ARG arcgis_version
LABEL org.opencontainers.image.authors="jroebuck@esri.com"
LABEL org.opencontainers.image.description="Jupyter Notebook with the latest version of the ArcGIS API for Python with arcgis_learn and its Linux dependencies preinstalled"

RUN conda install -c esri arcgis_learn=${arcgis_version} -y \
    && conda clean --all -f -y \
    && find /opt/conda -name __pycache__ -type d -exec rm -rf {} +