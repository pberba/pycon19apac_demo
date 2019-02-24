#! /usr/bin/python

import sys
import webbrowser
import subprocess


def google_lookup(query, browser='firefox'):
    url = 'https://www.google.com/search?q={}'.format(query)
    webbrowser.get(browser).open(url)


if __name__ == '__main__':
    data = subprocess.check_output('xsel')
    google_lookup(data)
