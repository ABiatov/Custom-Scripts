#!/bin/sh
# конвентирует и сжимает ПНГ-файлы в жипеги, потом собираети их в многостраничный ПДФ book.pdf, порядок определяет  по имени файла
#  
# путь где лежат исходные ПНГ-файлы /home/user/Documents/BookPNG

# cd /home/user/Documents/BookPNG

# mkdir -p ./jpg_dir/pdf_dir
# mkdir ./png_dir
for fname1 in *.png
do fname2="$(basename $fname1 .png)"
gm convert $fname2.png -compress JPEG ./jpg_dir/$fname2.jpg
done
cd ./jpg_dir
convert *.jpg -adjoin ./pdf_dir/book.pdf
cd ..
mv ./jpg_dir/pdf_dir ./pdf_dir
mv ./*.png ./png_dir/

