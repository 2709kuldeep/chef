#!/bin/bash
n=$1 
i=1 
while [ $i -le $n ] 
do 
if [ $((i%2)) -eq 0 ] 
then 
echo $i 
fi 
i=`expr $i + 1` 
done

