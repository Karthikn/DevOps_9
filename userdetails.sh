#!/bin/bash
read -p "Enter your name : " name
read -p "Enter your age : " age

echo "Hello $name, Your Age is $age!"

if [ "$age" -eq 18 ] || [ "$age" -gt 18 ];then
	echo "You are eligible to drink"
else 
	echo "Not allowed to drink"
 fi
