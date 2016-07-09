#!/bin/sh

if [ $# -ne 2 ]; then
    echo "false";
    exit 1;
fi

echo "$2" | kinit $1 > /dev/null
echo "token: `klist`"
echo "Students"
