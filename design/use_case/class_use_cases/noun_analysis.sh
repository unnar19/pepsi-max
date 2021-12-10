#!/bin/bash

# cat ../objects.txt | xargs -n 1 echo "Nr,Lýsing,Forgangur"

cat ../objects.txt | while read line
do
    echo "\\"'textbf{Nr},'"\\"'textbf{Lýsing},'"\\"'textbf{Forgangur},'"\\"'textbf{Fall}' > 1_EDIT/$line.csv
done

cat ../encoding.csv | while read line
do 
    case $line in
        *"erkbeið"*)
        echo $line ",()">> 1_EDIT/Ticket.csv
    esac
    case $line in
        *"otand"*)
        echo $line ",()">> 1_EDIT/Employee.csv
    esac
    case $line in
        *"fangast"*)
        echo $line ",()">> 1_EDIT/Destination.csv
    esac
    case $line in
        *"kýrsl"*)
        echo $line ",()">> 1_EDIT/Report.csv
    esac
    case $line in
        *"asteign"*)
        echo $line ",()">> 1_EDIT/RealEstate.csv
    esac
    case $line in
        *"erktak"*)
        echo $line ",()">> 1_EDIT/Contractor.csv
    esac
done
