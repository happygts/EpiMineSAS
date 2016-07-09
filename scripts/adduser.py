#!/usr/bin/env python

import sys
import subprocess
import json

if len(sys.argv) != 4:
    print "Usage: " + sys.argv[0] + " token username password"
    exit(1)

cmd_line="echo " + sys.argv[2] + " | kinit " + sys.argv[1] + " 2>&1 > /dev/null"

try:
    subprocess.check_output(cmd_line, shell=True)
except subprocess.CalledProcessError:
    print "Wrong credentials"
    exit(1)
out=subprocess.check_output("klist", shell=True)
print json.dumps({'token': out, 'type': "user"})
