#!/bin/sh
# скачивает OSM-данные с http://overpass-api.de/api/xapi? по охвату квадрата Харьковской области по фильтру тегов заповедных территорий.обрезает по маске Харьковской области из файла "./shp/boundary_*.shp" и сохраняет в KML-файл
# chmod +x osm2kml-pzf-kharkov.sh
# step 1. delete old file KML
rm ./pzf_kharkov_polygon.kml
# step 2. create temp dir
mkdir -p ./temp/
# step 3. Download OSM from XAPI.openstreetmap
wget --timeout=$(( 24 * 60 * 60 )) -O ./temp/data.osm http://overpass-api.de/api/xapi?*[bbox=34.8561,48.5312,38.0936,50.4594][boundary=protected_area\|national_park\|leisure=nature_reserve][@meta]
# step 4. converting OSM to KML
ogr2ogr -skipfailures -s_srs "EPSG:4326" -t_srs "EPSG:4326" -nlt MULTIPOLYGON -sql "SELECT * FROM multipolygons WHERE OGR_GEOMETRY='MULTIPOLYGON'" -clipsrc ./shp/boundary_kh.shp -lco ENCODING=UTF-8 -f "KML" -overwrite ./pzf_kharkov_polygon.kml  ./temp/data.osm
# step 5. delete temp dir
rm -r ./temp
