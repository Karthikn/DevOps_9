#!/bin/bash

echo "Enter the first number:"
read a
echo "Enter the second number:"
read b

if [ $a -gt $b ]; then
    echo "$a is greater than $b"
elif [ $a -lt $b ]; then
    echo "$a is less than $b"
else
     echo "a equals b"
fi
