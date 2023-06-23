#!/bin/bash

file=$2
mess=$3

git_aasup()
{
	git add $file ; git commit -m $mess
}

if test "$1"="aasup"
then
	git_aasup
fi
