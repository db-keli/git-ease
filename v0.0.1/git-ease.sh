#!/bin/bash

file=$2
mess=$3

afca(){
	git add $file
	git commit -m "$mess"
}

aca(){
	git add .
	git commit -m "$mess"
}

if [ "$1" == "-f" ];
then
	afca
elif [ "$1" == "-a" ];
then
	aca
fi

