#! /usr/bin/python

"""
from_buffer

see README for usage
"""


import sys # .argv
from time import sleep


### constants
HOW_OFTEN_TO_READ = .5 # sec




### parse args
buffer_file = str(sys.argv[1])



while True:

    try:

        with open(buffer_file, 'r+') as fil:
            text = fil.read()
            fil.truncate() # empties it

        print text

    except IOError:
        # file doesn't exist yet. README mandates that that's perfectly fine usage (for ease of use, allows running from before to without an explicit touch)
        pass

    sleep(HOW_OFTEN_TO_READ)


