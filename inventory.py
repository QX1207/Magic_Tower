# Course: CS 30
# Period: 1
# Date created: 20/02/13
# Date last modified: 20/02/23
# Name: Qian Xiang
# Description: inventory for this game that store my weapon's name, data, and
# description
# Small tips: the inventory was build as lists. they will be changed to be
# dictionary after.

# import random
import random


# a list of common weapon in the game
commonWeapon = ['Wood Sword', 'Stone Sword', 'Bone Knife', 'Stone Knife',
                'Wood Knife', 'Stone Hatchet', 'Wood Dragger', 'Stone Dragger'
                'Broken Bow and Arrow - Dragon and Triger',
                'Wood Bow and Arrow']
# a list of rare weapon in the game
rareWeapon = ["Ice Wand - Frozen Ghost", "Wind Sword - Death Zone",
              "Fire Dagger - Fire Punishment", "Dark Dragger - Infinite",
              "Mechanical Umbrella - Thousands of Organ"]
# a list of epic weapon in the game
epicWeapon = ["Star Wand - Final Justice", "Death Stone - Dark Hallow",
              "Unknown Sword - Broken Sword from the Stone"]
# a list of legenary weapon in the game
legendaryWeapon = ["Chaos Mirror"]


# print the list "commonWeapon" to verify it performs properly
print(commonWeapon)
# print the list "rareWeapon" tol; verify it performs properly
print(rareWeapon)
# print the list "epicWeapon" to verify it performs properly
print(epicWeapon)
# print the list "legendaryWeapon" to verify it performs properly
print(legendaryWeapon)
# All the items in list "commonWeapon" are printed out in sentence
# using f-strings
print("You found a weapon in a chest.",
      f"You get a common weapon {random.choice(commonWeapon)}!")


# All the items in list "rareWeapon" are printed out in sentence
# using f-strings
print("You found a weapon on the monster's body.",
      f"You get a rare weapon {random.choice(rareWeapon)}!")


# All the items in list "epicWeapon" are printed out in sentence
# using f-strings
print("You killed the boss in this room.",
      f"You get a epic weapon {random.choice(epicWeapon)}!")


# All the items in list "epicWeapon" are printed out in sentence
# using f-strings
print("You successfully opened the treasure's door with three epic",
      "weapons and a historical reels.",
      f"You get a terrible weapon {legendaryWeapon}!")


# Use append() to add one new weapon to the list commonWeapon.
commonWeapon.append("Sword of Glory - Light")
# print the list after append.
print(commonWeapon)


# Use insert() to add one new weapon to the beginning of my list.
commonWeapon.insert(0, "Unknown Broken Sword with monsters' blood")
# print the list after insert.
print(commonWeapon)


# Use del() method to delete a weapoon in my list
del commonWeapon[0]
# print the list after delete a element.
print(commonWeapon)


# Use pop() to print a message to the player.
print("Sorry. The special weapon ", commonWeapon.pop(0), "was destoryed.")


# Use remove() to remove a epic weapon
epicWeapon.remove("Star Wand - Final Justice")
# print the list after remove a element.
print(epicWeapon)


# Store my list rareWeapon alphabetically
rareWeapon.sort()
# print the list after sort
print(rareWeapon)


# print a sorted list rareWeapon into reverse chronological order
print(sorted(rareWeapon, reverse=True))

# use reverse() to print the list commonWeapon into reverse chronological order
commonWeapon.reverse()
# print the list commonWeapon after reverse
print(commonWeapon)

# Use len() to count the number of my list commonWeapon
len(commonWeapon)

# Use index() to create a numerical list
numerical_list = []
for a in commonWeapon:
    p = commonWeapon.index(a)
    numerical_list.append(p)
print(numerical_list)

# Use index to find the weapons' posistion in my list
index = [1, 3, 7]
play_weapon = [commonWeapon[i] for i in index]
player_weapon = []
for i in index:
    player_weapon.append(commonWeapon[i])

print(player_weapon)
