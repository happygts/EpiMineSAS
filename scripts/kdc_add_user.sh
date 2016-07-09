#!/bin/sh

function usage
{
    echo "Usage: $0 username password account_type"
}

if [ $# -ne 3 ]; then
    usage
    exit 1
fi

if [ ${#2} -lt 8 ]; then
    echo "Password should have 8 character min"
    exit 1
fi

if [ "$3" != "Students" ] && [ "$3" != "Direction" ] && [ "$3" != "Adm" ] && [ "$3" != "SysAdmin" ]; then
    echo "Invalid account type"
    exit 1
fi

useradd $1
echo -e "$2\n$2" | passwd $1
echo -e "$2\n$2" | kadmin.local -q "addprinc $1"
