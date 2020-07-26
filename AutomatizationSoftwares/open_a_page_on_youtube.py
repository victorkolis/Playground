#!/usr/bin/env python3

import webbrowser
import time

def linkOpener(link):
    openingSentence = 'loading...'
    for i in openingSentence:
        print(i, end=' ')
        time.sleep(.07)
    time.sleep(3)
    webbrowser.open(link)
    

link = input('please enter your link here: ')

linkOpener(link)
