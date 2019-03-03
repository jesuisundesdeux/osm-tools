#!/bin/bash

# 2019 - Bruno Adele <brunoadele@gmail.com> #JeSuisUnDesDeux team

# Make python environment
python -mvenv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt

docker run --rm -it \
    -e PLANET_URL="https://download.geofabrik.de/europe/france-latest.osm.bz2" \
    -e FLUSH_SIZE=4 \
    -p 80:80 -v $(pwd)/data:/data badele/overpass-api:0.7.55
