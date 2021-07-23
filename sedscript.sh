#!/bin/sh
path=/home/devopsadmin/sample.txt
#replacing single word in a line"
echo "I am tom" | sed 's/tom/john/'
sed 's/work/play/' $path
echo "-------------------"
#replacing all the occurrences of matched word
sed 's/study/learn/g' $path
echo "-------------------"
#deleting line if containing the particular word
sed '/while/d' $path
echo "-------------------"
#deleting a particular word color from a line
sed '3s/color//g' $path
echo "-------------------"
#dispalying specific column value
sed '4s/[^:]* \([^:]* \)[^:]*/\1/' $path
sed 'i\the saying' $path
