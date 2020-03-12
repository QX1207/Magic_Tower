# Course: CS 30
# Period: 1
# Date created: 20/01/30
# Date last modified: 20/01/30
# Name: Qian Xiang
# Description: psceudocodes for this game

# All importing file and python standard library:
# import sys
# import time

# Print out the title of game
# Two selections:
# First: Just print the sentence "Welcome to the Magic Tower"
# I would like to print it slowly that create a little bit visual
# effect
# import sys
# import time
#
# def print_slow(str):
#     for char in str:
#         time.sleep(.3)
#         sys.stdout.write(char)
#         sys.stdout.flush()
#
# print_slow('Welcome to the Magic Tower')
# Second: Print out the following code
# title =
# r"""                                _
#       __       __                  (_)
#      /  \     /  \     __ _   __ _  _   ___
#     /  _ \   / _  \   / _` | / _` || | / _/
#    /  / \ \_/ / \  \ | (_| || (_| || || (__
#   /  /   \   /   \  \ \__,_| \__, ||_| \__/
#  /  /     \_/     \  \         _/ |
# /__/               \__\       |___/
#           ____
# _________/   /
# |____   ____/
#     |  |
#     |  |  ___ __    _    __ ___   _ __
#     |  | / _ \\ \  /_\  / // _ \| '__/
#     |  || (_) |\ \// \\/ /|  __/| |
#     \__/ \___/  \_/   \_/  \___||_|
# """
# print(title)

# print introduce introduce text
# print("...")
# Set up the start menu
# choices on menu:
# *characters
# *map
# *quit
# *game information

# if the player select the *characters
# then print out some informations about characters
# character #1:
# name: knight Sir William Marshal
# background story: (construction)
# beginning weapon: Wood Sword, Stone Sword, Bone Knife, Stone Knife,
# Wood Knife, or Stone Hatchet.
# ability: (construction)
# attack damage: 26
# health: 250

# character #2:
# name: mage Alastor Moody
# background story: (construction)
# beginning weapon: Ice Wand - Frozen Ghost or
# Mechanical Umbrella - Thousands of Organ
# ability: Ignore enemy armor. (Alastor Moody is a great mage from British.
# His power can destory other armor. He is a good choice to defeat high armor
# monster, although his body is weak.)
# attack damage: 30
# health: 200
# after the player select the character. jump to the commonWeapon

# describe the background story of the map
# map name: symbol of water--Nereus's wealth
# story: (construction)
# task: 1st: find the password
#       2nd: beat the Nereus's incarnation, then find the door
#       3rd: enter the correct password, then win the game
# map craft:
#                    Top
#       password  | a chest   |   start point
#       shark     | sea triger|   black turtle
#       hagfish S | Nereus    |   evil fish king
#                    Bottom

# then enter the game(begin)

# if the player select the *map
# just print out the map above
# after select, the player can select the characters
# print out characters' information
# after select, enter the game(begin)

# print the plot
# plot: (construction)
# choice your movement: Upstair, Downstair, Left, or Right
# after choice, enter the new room
# print out the plot
# plot: (construction)
# print out monster's name
# print out monster's hp
# 4 choice to decide your reaction, attack(make damage to the boss),
# dodge(dodge the boss's attack and make a few damage to the boss, maybe fail),
# use your weapon ability, escape(back to the last room and print the
# movement chooses again)
# if you died in the room, you will have two choises: 1. replay the game in the
# room, then print out 4 choice again. 2. give up and fail in the game, then
# print out the statement for loser.)
# def fail(died):
#     for die in died:
#         time.sleep(.5)
#         sys.stdout.write(die)
#         sys.stdout.flush()
# fail('You was kill by the(). The tower rab your power and disolve your body.'
#     )
# If you win, you will get a random weapon and enter a plot that decide
# by the boss you beat.
# --> loop

# if you enter the passwor room, you will do the same process as other
# you just get a password after you win the boss.

# if you enter the Nereus' room
# --> loop
# after you beat the boss, you will have a oppturnity to enter the password
# then win the game. if the password is right, you will win the game. if the
# password is wrong, you will fail the game.

# --> win
# print out plot: (construction)

# --> fail
# print out plot: (construction)
# print out the statement for loser.


# boss information: (construction)
# 1st:
# 2st:
# 3st:
# 4th:
# 5th:
# 6th:
# 7th:

# inventory information:
# weapon: (construction)
'name': 'Wood Sword',
'description': 'A long sword that made by wood.',
'damage': '10',
'name': 'Stone Sword',
'description': 'A tough sword that made by stone',
'damage': '15',
'name': 'Bone Sword',
'description': 'A mysterious sword with snake blood',
'damage': '18',
'name': 'Stone Knife',
'description': 'A stone knife that look like fish',
'damage': '8',
'name': 'Wood Knife',
'description': 'A toy',
'damage': '6',
