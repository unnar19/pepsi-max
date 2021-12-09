#!/bin/bash

# This script generates a .tex and .pdf file from Windows-ANSI encoded .csv files

iconv -f "windows-1252" -t "UTF-8" all_use_cases.csv -o encoding_temp.csv &&

csv2latex encoding_temp.csv > all_use_cases.tex &&

sed -i 's/|l|l|l|/|c|p{10cm}|c|/' all_use_cases.tex &&

pdflatex -halt-on-error all_use_cases.tex