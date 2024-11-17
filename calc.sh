#!/bin/bash

read -p "Enter Number A: " A
read -p "Enter Number B: " B

# Performing arithmetic operations
add=$((A + B))
sub=$((A - B))
mul=$((A * B))
div=$((A / B))

echo "add = $add, sub = $sub, mul = $mul, div = $div"
