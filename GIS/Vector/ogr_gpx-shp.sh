#!/bin/sh
# chmod +x ogr_gpx-shp.sh


for fname1 in *.gpx
do fname2="$(basename $fname1 .gpx)"
ogr2ogr -skipfailures -s_srs "EPSG:4326" -t_srs "EPSG:4326" -select "name,cmt,ele,time" -f "ESRI Shapefile" ./shp-$fname2 $fname1
# ogr2ogr -skipfailures -s_srs "EPSG:4326" -t_srs "EPSG:4326" -f "ESRI Shapefile" ./shp-$fname2 $fname1
# ogr2ogr -skipfailures -s_srs "EPSG:4326" -t_srs "EPSG:4326" -f "ESRI Shapefile" -nlt "POINT" ./shp/$fname2 $fname1
# ogr2ogr -skipfailures -s_srs "EPSG:4326" -t_srs "EPSG:4326" -f "ESRI Shapefile" -nlt "LINESTRING" ./shp/$fname2 $fname1
rm ./shp-$fname2/routes.*
rm ./shp-$fname2/route_points.*
rm ./shp-$fname2/track_points.*
# rm ./shp-$fname2/tracks.*
# rm ./shp-$fname2/waypoints.*
done



# ogr2ogr -f CSV $fname2 $fname2.gpx -lco GEOMETRY=AS_XYZ
