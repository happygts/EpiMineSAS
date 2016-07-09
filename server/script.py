#!/usr/bin/env python

import sys
import subprocess
import json

def connect(username, passwd):
    cmd_line="echo " + passwd + " | kinit " + username + " 2>&1 > /dev/null"
    try:
        subprocess.check_output(cmd_line, shell=True)
    except subprocess.CalledProcessError:
        return "Wrong credentials"
    out=subprocess.check_output("klist", shell=True)
    return json.dumps({'token': out, 'ok': 1, 'type': "user"})
