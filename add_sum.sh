#!/bin/bash

read -p "Enter the first number:" a
read -p "Enter the second number:" b

# Add the two numbers
sum=$((a + b))

# Display the result
echo "The sum is: $sum"

if [ $sum -gt 10 ]; then
    echo "Good"

elif [ $sum -eq 10 ]; then
    echo "Avg"
    
else
    echo "Below Avg"

fi
