#!/bin/sh
#finding bigger number from the passed arguments using if condition

if [ $1 -gt $2 ]
then
    echo $1 "is greater"
elif [ $1 -eq $2 ]
then
    echo $1 "&" $2 "are equal"
else
    echo $2 "is greater"
fi
#other parameters
echo the script name is $0
echo PID of script is $$
echo total arguments count is $#
echo last return code $?
echo all arguments $*
