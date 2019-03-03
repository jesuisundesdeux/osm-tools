# osm-tools
Tools for OSM datas manipulation

# Install app & datas requirements
Update `setup.sh` and execute below command
```
./setup.sh
```

# Run a local overpass server
```
docker run --rm -it \
    -e PLANET_FILE="france.osm.bz2" \
    -e FLUSH_SIZE=4 \
    -p 80:80 -v $(pwd)/data:/data badele/overpass-api
```

# Analyze cities and streets datas
```
source .virtualenv/bin/activate
./generate_summary.py
```
