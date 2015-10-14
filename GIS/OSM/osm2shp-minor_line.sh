#!/bin/sh
# скачивает OSM-данные с http://overpass-api.de/api/xapi? по охвату квадрата Харьковской области по фильтру тегов зpower=minor_line и обрезает по маске Харьковской области из файла "./shp/boundary_kh.shp" и сохраняет в shp-файл
# chmod +x osm2shp-minor_line.sh
# anton.biatov gmail.com
# http://gis-naturalist.blogspot.com

# step 0. delete old minor_line dir
rm -r ./minor_line/
# step 1. create temp dir
mkdir -p ./temp/
mkdir -p ./minor_line/
# step 2. Download OSM from XAPI.openstreetmap
wget --timeout=$(( 24 * 60 * 60 )) -O ./temp/data.osm http://overpass-api.de/api/xapi?*[bbox=34.8561,48.5312,38.0936,50.4594][power=minor_line][@meta]
# step 3. converting OSM to SHP
ogr2ogr -skipfailures -s_srs "EPSG:4326" -t_srs "EPSG:4326" -nlt "LINESTRING" -sql "SELECT * FROM lines WHERE OGR_GEOMETRY='LineString'" -clipsrc ./shp/boundary_kh.shp -lco ENCODING=UTF-8 -f "ESRI Shapefile" -overwrite ./minor_line/minor_line.shp  ./temp/data.osm
# step 4. delete temp dir
rm -r ./temp
