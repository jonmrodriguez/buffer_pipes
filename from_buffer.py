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
            
            # empty the file
            fil.seek(0) # arg is byte offset
            fil.truncate() # delete everything under and after the cursor

        print text, # the newline, if desired at all, goes in the buffer file

    except IOError:
        # file doesn't exist yet. README mandates that that's perfectly fine usage (for ease of use, allows running from before to without an explicit touch)
        pass

    sleep(HOW_OFTEN_TO_READ)


