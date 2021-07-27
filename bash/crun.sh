#!/usr/bin/env bash

echo crun.sh command = "$0"
#echo "#"="$#"

BASE_NAME=$(basename "$0")
#echo BASE_NAME=$BASE_NAME
#echo parameters"$@"
SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")
#echo SCRIPT_PATH="$SCRIPT_PATH"

EXE_FILE="$BASE_NAME"

    if [ -f "$SCRIPT_PATH""/${BASE_NAME}" ]; then
        EXE_FILE="$SCRIPT_PATH""/${BASE_NAME}"
        #echo EXE_FILE="$EXE_FILE"
        "$EXE_FILE" "$@"

        exit $?
    fi
