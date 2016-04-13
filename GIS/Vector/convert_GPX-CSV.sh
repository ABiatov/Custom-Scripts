#!/bin/sh
# Создает CSV-файл в папке с GPX-файлом, запускать из папки с GPX-файлом
# перед запуском добавит право на выполнение: chmod +x convert_GPX-CSV.sh
# работает при условии, что в имени gpx-файла отсутствуют пробелы

for fname1 in *.gpx
do fname2="$(basename $fname1 .gpx)"
ogr2ogr -f CSV $fname2 $fname2.gpx -lco GEOMETRY=AS_XY
mv ./$fname2/waypoints.csv ./$fname2.csv
rm -r ./$fname2
done
