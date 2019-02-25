#!/bin/bash

# 2019 - Bruno Adele <brunoadele@gmail.com> #JeSuisUnDesDeux team

DATAS="datas"
OPTIONS="--drop-author --drop-version"

########################
# Get regions boundary
########################
if [ ! -f "${DATAS}/osm/regions-relations.o5m" ]; then
    echo "Get regions boundary"
    ./osmfilter "${DATAS}/osm/france.o5m" ${OPTIONS} --keep= --keep-relations='admin_level=4 AND boundary=administrative' -o="${DATAS}/osm/regions-relations.o5m"
fi

########################
# Generate regions list
########################
if [ ! -f "${DATAS}/summary/regions-list.csv" ]; then
    if [ ! -f "${DATAS}/osm/regions-list.o5m" ]; then
        echo "Generate Regions CSV list"
        ./osmfilter "${DATAS}/osm/regions-relations.o5m" ${OPTIONS} --drop-ways --ignore-dependencies --keep='admin_level=4 AND ref:INSEE= AND ref:NUTS' --drop-nodes -o="${DATAS}/osm/regions-list.o5m"

        ./osmconvert "${DATAS}/osm/regions-list.o5m" --csv="@id @lon @lat name population source:population" --csv-headline --csv-separator=';' -o="${DATAS}/summary/regions-list.csv"
        rm "${DATAS}/osm/regions-list.o5m"
    fi
fi

########################
# Region Polygon
########################

is_number='^[0-9]+$'
while IFS=';' read -r id lon lat name population source_population; do
    name_norm=$(echo "${name}" | iconv -f utf8 -t ascii//TRANSLIT//IGNORE | tr " " "-")

    if [[ $id =~ $is_number ]] ; then
        if [ ! -f "${DATAS}/osm/regions-${name_norm}.o5m" ]; then
            echo "Generate polygon for ${name_norm}(${id})"
            if [ ! -f "${DATAS}/osm/regions-poly-${name_norm}.o5m" ]; then
                ./osmfilter "${DATAS}/osm/regions-relations.o5m" ${OPTIONS} --keep="@id=${id}" -o="${DATAS}/osm/regions-poly-${name_norm}.o5m"
                
                generated=0
                idx=2
                while [ $generated -eq 0 -a $idx -lt 2000 ]
                do
                    echo "Try to generate polygon for ${name_norm} with ${idx} simplify"
                    ./osmrelpoly --simplify=${idx} "${DATAS}/osm/regions-poly-${name_norm}.o5m" -o="${DATAS}/osm/regions-poly-${name_norm}.poly"
                    size=$(stat -c %s "${DATAS}/osm/regions-poly-${name_norm}.poly")
                    nblines=$(wc -l < "${DATAS}/osm/regions-poly-${name_norm}.poly")
                    echo ""
                    echo "### NBLINES: $nblines / SIZE: $size"
                    echo "Try to Split region data for ${name_norm}"
                    ./osmconvert "${DATAS}/osm/france.o5m" -B="${DATAS}/osm/regions-poly-${name_norm}.poly" -o="${DATAS}/osm/regions-${name_norm}.o5m" > /dev/null
                    if [ $? -eq 0 ]; then
                        ./osmconvert "${DATAS}/osm/regions-${name_norm}.o5m" -o="${DATAS}/osm/regions-${name_norm}.osm"
                        generated=1
                    fi

                    idx=$[$idx+1]
                done
            fi
        fi
    fi    
done < ${DATAS}/summary/regions-list.csv
