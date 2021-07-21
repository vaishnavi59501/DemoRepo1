#!/bin/sh
#finding bigger number from the passed arguments using if condition

if [ $1 -gt $2 ]
then
    echo $1 "is greater"
else
    echo $2 "is greater"
fi

echo the script name is $0
echo total arguments count is $#
echo last return code $?
echo all arguments $*
