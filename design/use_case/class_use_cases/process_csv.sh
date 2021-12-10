#!/bin/bash

rm -rf all_tables.tex
cat ../objects.txt | while read line

do 
    # Convert .csv to .tex
    csv2latex 1_EDIT/$line.csv > 2_USE/$line.tex

    # Replace alignment section with special parameters
    sed -i 's/|l|l|/|c|p{10cm}|/' 2_USE/$line.tex

    # copy table to temp file
    tail -n +4 2_USE/$line.tex > tex_format.txt

    # Delete \end{document} for correct placement of \¢aption
    head -n -1 tex_format.txt | sponge tex_format.txt

    # Add caption and label entry to .tex
    echo '\\caption{Gagnatag: '"$line"'}' | tee -a tex_format.txt

    echo '\\label{tab:'"$line"'}\\end{document}' | tee -a tex_format.txt
    
    # Append to main file
    cat tex_format.txt >> all_tables.tex

    # Compile pdf
    # pdflatex -halt-on-error -output-directory 3_VIEW 2_USE/$line.tex
done

# Replace document entries in main file
sed -i 's/begin{document}/begin{table}[h!]\\centering/' all_tables.tex
sed -i 's/end{document}/end{table}/' all_tables.tex



