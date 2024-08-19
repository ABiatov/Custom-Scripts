#!/bin/sh
# Создает CSV-файл в папке с GPX-файлом, запускать из папки с GPX-файлом
# перед запуском добавит првао на выполнение: chmod +x convert_GPX-CSV.sh
# работает при условии, что в имени gpx-файла отсутствуют пробелы
# /home/user/Maps/WD/temp/ - путь к директории с  GPX-файлами

# cd /home/user/Maps/WD/temp/
for fname1 in *.gpx
do fname2="$(basename $fname1 .gpx)"
ogr2ogr -f CSV $fname2 $fname2.gpx -lco GEOMETRY=AS_XYZ
mv ./$fname2/waypoints.csv ./$fname2.csv
rmdir ./$fname2
done
# rm convert_GPX-CSV.sh
