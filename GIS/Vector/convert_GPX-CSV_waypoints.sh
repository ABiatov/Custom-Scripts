#!/bin/sh
# Создает CSV-файлы в папке с GPX-файлами, запускать из папки с GPX-файлами
# перед запуском добавит право на выполнение: chmod +x ./convert_GPX-CSV_waypoints.sh
# работает при условии, что в имени gpx-файлов отсутствуют пробелы

for fname1 in *.gpx
do fname2="$(basename $fname1 .gpx)"
ogr2ogr -f CSV $fname2 $fname2.gpx -lco GEOMETRY=AS_XY
mv ./$fname2/waypoints.csv ./$fname2.csv
rm -r ./$fname2
done
