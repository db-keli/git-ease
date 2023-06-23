#!/bin/bash

if [ "$(id -u)" != "0" ]
then 
	echo "You are not the root user"
	exit 1
fi

GIT_EASE="ge"

BIN_PATH="/bin"

echo -e "Installing binaries"

cp "${GIT_EASE}.sh" "${BIN_PATH}"

mv "${BIN_PATH}/${GIT_EASE}.sh" "${BIN_PATH}/${GIT_EASE}"

chmod 777 "${BIN_PATH}/${GIT_EASE}"

echo -e "Done"
