# Class: CS 30
# Period: 1
# Date created: 2020-02-07
# Date last modified: 2020-03-11
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


# create a nested dictionary (a dictionary in a dictionary) for the characters
# number of character is use to count the # of character we have and help us
# to create other code easier
characters = {
             'Knight':{
             'number': '#1', 'name': 'Sir William Marshal',
             'background story': ' ',
             'beginning weapon': 'Wood Sword, Stone Sword, Bone Knife,'
             ' Stone Knife, Wood Knife, or Stone Hatchet',
             'ability': ' ',
             'attack damage': '26',
             'health': '250'},
             'Mage':{
             'number': '#2', 'name': 'Alastor Moody',
             'background story': ' ',
             'beginning weapon': 'Mechanical Umbrella - Thousands of Organ',
             'ability': 'Ignore enemy armor. (Alastor Moody is a great mage '
             'from British. His power can destory other armor. He is a good '
             'choice to defeat high armor monster, though his body '
             'is weak.)',
             'attack damage': '30',
             'health': '200'}
             }

# use some data from the above dictionary that it can be some variable to use.
# use for-loop to print out my statement about characters line by line
for characters, characters_info in characters.items():
    number = characters_info["number"]
    print(f"\nCharacters {number}: {characters}")
    name = characters_info['name']
    weapon = characters_info['beginning weapon']
    ability = characters_info['ability']
    health = characters_info["health"]
    damage = characters_info["attack damage"]
    print(f"\tName: {name.title()}")
    print(f"\tAblility: {ability}")
    print(f"\tCharacter's weapon inventory: {weapon}")
    print(f"\t{characters} has {health} health point")
    print(f"\tBasic Attack Damage: {damage}")
