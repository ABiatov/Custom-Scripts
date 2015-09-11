#!/bin/sh
# chmod +x ./convert_PNG-TIF_CMYK.sh

for fname1 in *.png
do fname2="$(basename $fname1 .png)"
convert -colorspace CMYK $fname2.png $fname2.tif
done
