#!/bin/sh

# chmod +x ./write_CRS_WGS84_in_raster.sh
# ./write_CRS_WGS84_in_raster.sh

mkdir WGS_84

for fname1 in ./*.tif
do fname2="$(basename $fname1 .tif)"

gdal_translate -a_srs EPSG:4326 $fname2.tif ./WGS_84/$fname2.tif

done

ls -l ./WGS_84

