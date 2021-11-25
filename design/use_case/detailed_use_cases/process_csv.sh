#!/bin/bash

# This script generates .tex and .pdf files from Windows-ANSI encoded .csv files

# Number of use cases is number of files in directory
# subtracted by 2 (use_case_base and encoding_temp)
num=$(($(ls ./1_EDIT | wc -l)-2))

for i in $(seq 1 $num)

do 
    iconv -f "windows-1252" -t "UTF-8" 1_EDIT/use_case_$i.csv -o encoding_temp.csv
    csv2latex encoding_temp.csv > 2_USE/use_case_$i.tex &&
    sed -i 's/|l|l|/|c|p{10cm}|/' 2_USE/use_case_$i.tex &&
    pdflatex -halt-on-error -output-directory 3_VIEW 2_USE/use_case_$i.tex
done