#!/bin/sh
# chmod +x ./convert_pdf2jpg.sh
# https://gis-naturalist.blogspot.com/

# Конвертирует pdf-файл в изображения jpg в 100% качеством постранично 
# в новую папку, которую называет по имени исходного pdf-файла.

for fname1 in *.pdf
do fname2="$(basename $fname1 .pdf)"
mkdir ./$fname2
convert -units PixelsPerInch $fname1 -resample 300 -compress JPEG -quality 100% ./$fname2/$fname2.jpg
done
