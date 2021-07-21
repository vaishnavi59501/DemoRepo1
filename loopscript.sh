#!/bin/sh
#shell variables
index=1
#using while loop to print 1 to 15 integers
while [ $index -le 15 ]
do
  echo $index
  index=$(($index + 1))
done

#using for loop to print 1 to 15 integers
for ((i=1;i<=15;i++))
do
  echo $i
done
