#!/bin/sh

# chmod +x ./timeseries.sh
# ./timeseries.sh

for fname1 in ./*.csv
do fname2="$(basename $fname1 .csv)"
cp ./$fname2.csv ./data.csv
./timeseries.r
./timeseries_smooth.r
mv ./time_seria.png ./$fname2.png
mv ./time_seria_smooth.png ./${fname2}_smooth.png
rm ./data.csv
rm ./Rplots.pdf
done


