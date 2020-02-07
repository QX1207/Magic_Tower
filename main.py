# Class: CS 30
# Period: 1
# Date created: 2020-02-07
# Date last modified: 2020-02-07
# Name: Qian Xiang
# Description: main.py in my text base adventure game that combine other file
# and run the game


# import python standard library
import sys
import time


# defined my printing speed
def print_slow(str):
    for char in str:
        time.sleep(.3)
        sys.stdout.write(char)
        sys.stdout.flush()

# print the sentence
print_slow('Welcome to the Magic Tower!')
