#! /usr/bin/python

"""
see README for usage
"""


import sys # .argv
from time import sleep


### parse args
buffer_file = str(sys.argv[1])



while True:
    try:
        text = raw_input()
    except EOFError:
        break

    # TODO using buffer_file + '.lock', allow multiple writers, e.g. to aggregate a bunch of stderrs into one console
    with open(buffer_file, 'a') as append_to:
        append_to.write(text)



