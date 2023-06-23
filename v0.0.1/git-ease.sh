#!/bin/bash

afca(){
	git add "$file"
	git commit -m "$mess"
}

aca(){
	git add .
	git commit -m "$mess"
}

push(){
	git push -u origin $branch
}


if [ "$1" == "-f" ];
then
	file=$2
	mess=$3
	afca
elif [ "$1" == "-a" ];
then
	file=$2
	mess=$3
	aca
elif [ "$1" == "-f" && $2 == "-p" ] || [  "$1" == "-p" && $2 == "-f" ];
then
	file=$3
	mess=$4
	afca
	echo Branch name:
	read branch
	push
elif [ "$1" == "-p" ];
then 
	echo branch name:
	read branch
	
	push
fi

