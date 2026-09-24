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

#creating the character
player, player_hp, attack, heal= classes[choice]
max_hp = player_hp


#picks a boss at random
boss_name = random.choice(list(bosses))
boss_hp, boss_attack, boss_special = bosses[boss_name]

print("Your character is ", player, "and your opponent is ", boss_name)

#the battle phase
while player_hp > 0 and boss_hp > 0:

    print("The battle has begun")
    print(player, "HP: ", player_hp)
    print(boss_name, "HP: ", boss_hp)
    print()
    print("Your options are; 1 for attack, 2 for special attack")
    print("3 to heal, and 4 to quit")

    action = input("Choose your action: ")

    if action == "1":
        #damage will be a random number inbetween the attack stat with a range of +-3
        damage = random.randint(attack-3, attack+3) 
        boss_hp -= damage
        print("\nYou dealt", damage, "damage to ", boss_name)

    elif action == "2":
        damage = random.randint(attack, attack +10)
        boss_hp -= damage
        print("\n You used a special attack you dealt", damage, "damage to ", boss_name)

    elif action == "3":
        old_hp = player_hp
        player_hp = min(player_hp + heal, max_hp)
        print("\nYou healed ", player_hp - old_hp, "HP")

    elif action == "4":
        print("\n you ran away from the battle")
        break

    if boss_hp <= 0:
        print("Yayy you defeated the boss, you win")
        break

    
