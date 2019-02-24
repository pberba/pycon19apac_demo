#! /usr/bin/python

import sys
import webbrowser


def google_lookup(query, browser='firefox'):
    url = 'https://www.google.com/search?q={}'.format(query)
    webbrowser.get(browser).open(url)


if __name__ == '__main__':
    args = sys.argv[1:]
    google_lookup(args[0])
