#! /usr/bin/python

import sys
import json

def prettify_json(obj):
    obj = json.loads(obj)
    return json.dumps(obj, indent=3) 

if __name__ == '__main__':
    print(prettify_json(sys.stdin.read()))