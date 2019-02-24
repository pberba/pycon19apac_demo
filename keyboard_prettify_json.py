#! /usr/bin/python

import sys
import json
import subprocess


def prettify_json(obj):
    obj = json.loads(obj)
    return json.dumps(obj, indent=3)


def clipboard(output):
    p = subprocess.Popen(['xsel', '-ib'], stdin=subprocess.PIPE)
    p.communicate(output)


if __name__ == '__main__':
    data = subprocess.check_output('xsel')
    output = prettify_json(data)
    clipboard(output)
