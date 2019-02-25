#!/bin/bash

# 2019 - Bruno Adele <brunoadele@gmail.com> #JeSuisUnDesDeux team

MAXPOLYGONS=200000
DATAS="datas"

mkdir -p "${DATAS}/osm"
mkdir -p "${DATAS}/summary"

# Donwload an compile osmconvert
if [ ! -f  osmconvert ]; then
    MAXLINE=12 echo "#define border__edge_M 60004" | 
    wget -O - http://m.m.i24.cc/osmconvert.c | sed "s/#define border__edge_M 60004/#define border__edge_M $MAXPOLYGONS/" | cc -x c - -lz -O3 -o osmconvert
    chmod 755 osmconvert
    rm 
fi

# Donwload an compile osmfilter
if [ ! -f  osmfilter ]; then
    wget -O - http://m.m.i24.cc/osmfilter.c |cc -x c - -O3 -o osmfilter
    chmod 755 osmfilter
fi

if [ ! -f  osmrelpoly ]; then
    wget -O - http://m.m.i24.cc/osmrelpoly.c |cc -x c - -O3 -o osmrelpoly
    chmod 755 osmrelpoly
fi

# Download OSM datas
if [ ! -f ${DATAS}/osm/france.o5m ]; then
    echo "Download OSM france datas"
    #wget -O ${DATAS}/france-latest.osm.pbf https://download.geofabrik.de/europe/france-latest.osm.pbf
    #wget -O ${DATAS}/osm/france-latest.osm.pbf http://download.openstreetmap.fr/extracts/merge/france_metro_dom_com_nc-latest.osm.pbf
    
    echo "Convert to o5m format"
    osmconvert ${DATAS}/osm/france-latest.osm.pbf -o=${DATAS}/osm/france.o5m

    echo "You can now delete ${DATAS}/france-latest.osm.pbf file"
fi
