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

push(){
	arg1=$1
	git push -u origin $1
}


if [ "$1" == "-f" ];
then
	afca
elif [ "$1" == "-a" ];
then
	aca
elif ["$1" == "-f" && $2 == "-p"];
then
	afca
	echo Branch name:
	read branch
	push branch
fi

