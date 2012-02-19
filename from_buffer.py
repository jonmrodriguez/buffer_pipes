#! /usr/bin/python

"""
see README for usage
"""


import sys # .argv
from time import sleep


### constants
HOW_OFTEN_TO_READ = .5 # sec




### parse args
buffer_file = str(sys.argv[1])



while True:

    with open(buffer_file, 'r') as fil:
        text = fil.read()

    print text

    sleep(HOW_OFTEN_TO_READ)


