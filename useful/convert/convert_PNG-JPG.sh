#!/bin/sh
# конвентирует ПНГ-файлы в жипеги со 100% качеством,
#  
# путь где лежат исходные ПНГ-файлы /home/user/Documents/PNG

# cd /home/user/Documents/PNG

mkdir -p ./jpg_dir/
# mkdir ./png_dir
for fname1 in *.png
do fname2="$(basename $fname1 .png)"
convert $fname2.png -compress JPEG -quality 100% ./jpg_dir/$fname2.jpg
done
