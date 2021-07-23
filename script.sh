#!/bin/sh
path=/home/devopsadmin/test.txt
#replacing single word in the below line
echo "hi everyone" | awk '{sub(/hi/,"hello"); print}'
echo "----------------------------"
#replacing all the occurrences of the matched word 
echo "learn while you learn" | awk '{gsub(/learn/,"study"); print}'
echo "----------------------------"
#deleting line containing particular word while
awk '!/while/' $path > tm.txt && mv tm.txt $path
awk '{print}' $path
echo "----------------------------"
#deleting word color 
echo "color green is cooling color" | awk '{print $2,$3,$4}'
echo "----------------------------"
#displaying last field of values
awk '{print $NF}' $path
echo "-----------------------------"
#displaying all the field values
awk '{print}' $path
echo "-----------------------------"
#adding row number at first column
awk '{print NR,$0}' $path
echo "-----------------------------"
#dispalying records in single line with output record separator
awk 'BEGIN{ORS="|"}{print}' $path
