#!/bin/bash

# This script generates .tex and .pdf files from Windows-ANSI encoded .csv files

# Number of use cases is number of files in directory
# subtracted by 2 (use_case_base and encoding_temp)

rm -rf all_tables.tex
num=$(($(ls ./1_EDIT | wc -l)-1))

for i in $(seq 1 $num)

do 

    # Change encoding for .tex
    iconv -f "windows-1252" -t "UTF-8" 1_EDIT/use_case_$i.csv -o encoding_temp.csv &&

    # Convert utf-8 encoded .csv to .tex
    csv2latex encoding_temp.csv > 2_USE/use_case_$i.tex &&

    # Replace alignment section with special parameters
    sed -i 's/|l|l|/|c|p{10cm}|/' 2_USE/use_case_$i.tex &&

    # Add caption and label entry to .tex
    echo '\caption{Use case '"$i"'}\label{tab:use_case_'"$i"'}' >> 2_USE/use_case_$i.tex

    # Append table to main table file
    tail -n +4 2_USE/use_case_$i.tex >> all_tables.tex

    # Compile pdf
    pdflatex -halt-on-error -output-directory 3_VIEW 2_USE/use_case_$i.tex
done

# Replace document entries in main file
sed -i 's/begin{document}/begin{table}[h!]\\centering/' all_tables.tex
sed -i 's/end{document}/end{table}/' all_tables.tex
