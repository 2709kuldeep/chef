#!/bin/bash
echo "Please enter a number"
read n
for (( i=1; $i <= $n; i++ ))
do
if [ $((i%2)) -ne 0 ]
then
echo $i
fi
done
