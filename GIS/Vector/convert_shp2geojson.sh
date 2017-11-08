#!/bin/sh
# Создает GeoJSON-файлы в папке с SHP-файлами, запускать из папки с SHP-файлами
# перед запуском добавит право на выполнение: chmod +x ./convert_shp2geojson.sh
# заменяем пробелы в именах файлов на нижние подчеркивания, следующюю строку исполняем отдельно в терминале в папке с  файлами. 
# IFS=$'\n'; for i in $(find $dir -depth -name '* *'); do mv $i $(dirname $i)/$(basename $i| tr ' ' '_'); done

# Создаем папкудля результатов 
mkdir geojson_files
# Конвертируем SHP в GeoJSON
for fname1 in ./*.shp
do fname2="$(basename $fname1 .shp)"
ogr2ogr -s_srs "EPSG:4326" -t_srs "EPSG:4326" -f GeoJSON -lco COORDINATE_PRECISION=5 ./geojson_files/$fname2.geojson $fname2.shp
done

