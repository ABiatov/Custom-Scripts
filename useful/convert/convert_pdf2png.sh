#!/bin/sh
# chmod +x ./convert_pdf2png.sh
# https://gis-naturalist.blogspot.com/
# Конвертирует pdf-файл в изображения png постранично 
# в новую папку, которую называет по имени исходного pdf-файла.

for fname1 in *.pdf
do fname2="$(basename $fname1 .pdf)"
mkdir ./$fname2
convert -units PixelsPerInch $fname1 -resample 300 ./$fname2/$fname2.png
done

