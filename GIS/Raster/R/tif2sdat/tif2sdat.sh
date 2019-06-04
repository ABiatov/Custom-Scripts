#!/bin/sh

# chmod +x ./tif2sdat.sh
# ./tif2sdat.sh

mkdir ./SDAT
for fname1 in ./*.tif
do fname2="$(basename $fname1 .tif)"
cp ./$fname2.tif ./temp.tif
./tif2sdat.r
mv ./rrrrr.sgrd ./SDAT/$fname2.sgrd
mv ./rrrrr.sdat ./SDAT/$fname2.sdat
rm ./temp.tif
done

ls -l ./SDAT