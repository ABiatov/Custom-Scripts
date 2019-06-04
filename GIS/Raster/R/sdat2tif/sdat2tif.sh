#!/bin/sh

# chmod +x ./sdat2tif.sh
# ./sdat2tif.sh

mkdir ./Output_TIF

for fname1 in ./*.sgrd
do fname2="$(basename $fname1 .sgrd)"
cp ./$fname2.sgrd ./temp.sgrd
cp ./$fname2.sdat ./temp.sdat
cp ./$fname2.mgrd ./temp.mgrd
./sdat2tif.r
mv ./temp.tif ./Output_TIF/$fname2.tif

rm ./temp.sgrd
rm ./temp.sdat
rm ./temp.mgrd

done

ls -l ./Output_TIF/

