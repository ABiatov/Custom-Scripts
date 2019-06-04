#!/bin/sh
mkdir ./ASCII_laers
for fname1 in ./*.tif
do fname2="$(basename $fname1 .tif)"
cp ./$fname2.tif ./temp.tif
./tif2asc.r
mv ./rrrrr.asc ./ASCII_laers/$fname2.asc
rm ./temp.tif
done