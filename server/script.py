#!/usr/bin/env python

import sys
import subprocess
import json

def connect(username, passwd):
    cmd_line = "echo " + passwd + " | kinit " + username + " 2>&1 > /dev/null"
    try:
        subprocess.check_output(cmd_line, shell=True)
    except subprocess.CalledProcessError:
        return "Wrong credentials"
    out=subprocess.check_output("klist", shell=True)
    return json.dumps({'token': out, 'ok': 1, 'type': "user"})
<<<<<<< HEAD

def user_list():
    cmd_line ="kadmin.local -q \"getprincs\""
    try:
        out = subprocess.check_output(cmd_line, shell=True)
    except subprocess.CalledProcessError:
        return "Wrong credentials"
    return json.dumps({'user_list': out})

def set_pwd(username, passwd):
    cmd_line = "kadmin.local -q \"cpw -pw <new" passwd + "> <" + username + ">\""
    try:
        subprocess.check_output(cmd_line, shell=True)
    except subprocess.CalledProcessError:
        return "Wrong credentials"
    return json.dumps({'status': 'ok'})

def add_user(username, passwd):
    cmd_line = "kadmin.local -q \"addprinc -pw <" + password + "> <" + username + ">\""
    try:
        out = subprocess.check_output(cmd_line, shell=True)
    except subprocess.CalledProcessError:
        return "Wrong credentials"
    return json.dumps({'status': 'ok'})
=======
>>>>>>> dd0d72373431400fd30a264fd70aec4795fe7dc2
