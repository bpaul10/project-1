'''
Program name: Boss Battle
Author: Bernard Paul
Purpose: Pick you character to defeat a random boss from a 
set selection
Date 9/23/26
'''

import random #use to generate random monsters for later

# Playable classes as a dictonary 
classes = {
    "1": ("Knight", 110, 25, 10),
    "2": ("Mage", 90, 30, 10)

}

#Bosses also as a dictoanry 
bosses = {
    "Fire Dragon": (150, 20, 30),
    "Shadow king": (90, 30, 40)
}

#Player promted to choose class
print("Choose a class 1 for Knight, 2 for Mage")
choice = input("Type 1 or 2: ")

#creates while loop incase player picks option not in selection
while choice not in classes:
    choice = input("You have to type 1 or 2 to pick between Knight or Mage")

