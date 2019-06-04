#!/bin/sh

# chmod +x ./sdat2sdat_Majority_filter.sh
# ./sdat2sdat_Majority_filter.sh

<< ////
library path: /usr/lib/x86_64-linux-gnu/saga/
library name: libgrid_filter
library     : Filter
Usage: saga_cmd grid_filter 6 [-INPUT <str>] [-RESULT <str>] [-MODE <str>] [-RADIUS <num>] [-THRESHOLD <double>]
  -INPUT:<str>       	Grid
	Grid (input)
  -RESULT:<str>      	Filtered Grid
	Grid (optional output)
  -MODE:<str>        	Search Mode
	Choice
	Available Choices:
	[0] Square
	[1] Circle
	Default: 1
  -RADIUS:<num>      	Radius
	Integer
	Minimum: 1
	Default: 1
  -THRESHOLD:<double>	Threshold [Percent]
	Floating point
	Minimum: 0.000000
	Maximum: 100.000000 
////

mkdir ./SDAT_filtred

for fname1 in ./*.sgrd
do fname2="$(basename $fname1 .sgrd)"

saga_cmd grid_filter "Majority Filter" -INPUT "$fname2.sgrd" -RESULT "./SDAT_filtred/$fname2.sgrd" -MODE 0 -RADIUS 1 -THRESHOLD 0.6

done

ls -l ./SDAT_filtred/

