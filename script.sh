#!/bin/bash
dir='tests'
file=$dir'/tests.txt'
output=$dir'/output.txt'
nb=$(wc -l < $file)
if [[ $@ =~ ^[0-9]+$ ]] && [[ $(($@ <= $nb)) == 1 ]]
then
	equation=$(sed $@'q;d' $file)
	./computor -v "$equation" > $output
	cat $output
	./computor -s "$equation"
else
	for ((var=1; var<=$nb; var++))
	do
		equation=$(sed $var'q;d' $file)
		./computor -v "$equation" > $output
		if [[ $(diff -N $output $dir'/solutions/'$var'.txt') == "" ]]
		then
			echo -e $var" :	\033[32m[OK]\033[0m	| $equation"
		else
			echo -e $var" :	\033[31m[KO]	| $equation\033[0m"
		fi
	done
fi
