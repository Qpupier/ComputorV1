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
		if [[ $(diff $output $dir'/solutions/'$var'.txt') == "" ]]
		then
			echo -e $var" :	\033[32m[OK]\033[0m"
		else
			echo -e $var" :	\033[31m[KO]\033[0m"
		fi
	done
fi
