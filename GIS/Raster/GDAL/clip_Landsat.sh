#!/bin/sh

# chmod +x ./clip_Landsat.sh

# Обрезка сценны Landsat послойно по маске из векторного шейп-файла лежащего в дирректории "mask-clip", результат сохраняется в директорию "clip-data" с добавлением суфикса "-clip" в название файла.
# Скрипт и папка с маской обрезки должна находится в папке с исходными слоями

mkdir -p ./clip-data
for fname1 in ./*.TIF
do fname2="$(basename $fname1 .TIF)"
gdalwarp -q -cutline ./mask-clip/*.shp -crop_to_cutline -of GTiff $fname1 ./clip-data/$fname2-clip.TIF
done
