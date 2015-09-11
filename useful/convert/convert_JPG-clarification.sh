#!/bin/sh
# пакетно  осветляет фотки
# chmod +x convert_JPG-osvetlenie.sh
# ./convert_JPG-osvetlenie.sh
# запускать из  папки с фотками
mkdir -p ./clarified_pictures-equalize/
mkdir -p ./clarified_pictures-normalize/
mkdir -p ./clarified_pictures-gamma_1.5/
mkdir -p ./clarified_pictures-gamma_2/
for fname1 in *.[Jj][Pp][Gg]
do fname2="$(basename $fname1 .[Jj][Pp][Gg])"
convert $fname1 -equalize -compress JPEG -quality 90% ./clarified_pictures-equalize/$fname2.jpg
convert $fname1 -normalize -compress JPEG -quality 90% ./clarified_pictures-normalize/$fname2.jpg
convert $fname1 -gamma 1.5 -compress JPEG -quality 90% ./clarified_pictures-gamma_1.5/$fname2.jpg
convert $fname1 -gamma 2 -compress JPEG -quality 90% ./clarified_pictures-gamma_2/$fname2.jpg

done
