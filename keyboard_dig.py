#! /usr/bin/python

import sys
import subprocess


def dig(domain):
    return subprocess.check_output(['dig', domain, '+short']).strip()


def pop_up(title, body):
    subprocess.call(['notify-send', title, body])


if __name__ == '__main__':
    data = subprocess.check_output('xsel')
    output = dig(data)
    pop_up(data, output)
