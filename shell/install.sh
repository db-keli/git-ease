#!/bin/bash

if [ "$(id -u)" != "0" ]
then 
	echo "You are not the root user"
	exit 1
fi

GIT_SQUASH="squash"

BIN_PATH="/bin"

echo -e "Installing binaries"

cp "${GIT_SQUASH}.sh" "${BIN_PATH}"

mv "${BIN_PATH}/${GIT_SQUASH}.sh" "${BIN_PATH}/${GIT_SQUASH}"

chmod 777 "${BIN_PATH}/${GIT_SQUASH}"

echo -e "Done"
