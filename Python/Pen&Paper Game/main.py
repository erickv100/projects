
#import libraries

import numpy as np
import random
import time

import tkinter as tk       


# %%

#initial sats

barbarian = {
    "health": np.random.randint(70,101),
    "weapon": "Common Axe",
    "weapon_damage": np.random.randint(1,10),
    "magical_damage": np.random.randint(1,5)
}

mage = {
    "health": np.random.randint(50,101),
    "weapon": "Common Staff",
    "weapon_damage": np.random.randint(1,5),
    "magical_damage": np.random.randint(1,10)
}

position = 0
final_position = 100

enemies = ["GOBLIN","WOLF","SKELETON","ZOMBIE","SNAKE","MEDUSA"]

# %%
#define functions

dice_number = ""

#TRHOW DICE

def throwdice():

    #get global varialbes
    global dice_number

    input("Press enter to throw dice")
    dice_number = np.random.randint(1,9)
    return dice_number

#FIND A NEW WEAPON-----------------------------------------------------------------------

def find_weapon():

    global character
    global character_name

    if character_name == "Barbarian":
        
        weapon_list = ["Thor's Hammer","Axe of Destruction","Excalibur"]
        weapon = np.random.randint(0,len(weapon_list))
        character["weapon"] = weapon_list[weapon]
        print(character["weapon"])
        character["weapon_damage"] = character["weapon_damage"] + np.random.randint(1,15)
        print(f"You found a new weapon: {character["weapon"]}. Your new weapon damage is {character['weapon_damage']}\n")
        return character["weapon"]
    
    else:
        
        weapon_list = ["Staff of Fire","Staff of Dark Magic","Staff of unlimited Power"]
        weapon = np.random.randint(0,len(weapon_list))
        character["weapon"] = weapon_list[weapon]
        print(character["weapon"])
        character["weapon_damage"] = character["weapon_damage"] + np.random.randint(1,15)
        print(f"You found a new weapon: {weapon_list[0]}. Your new weapon damage is {character['weapon_damage']}\n")
        return character["weapon"]
    

    

#MOVE FORWARD----------------------------------------------------------------------------

def move_forward():
    
    #call global variables
    global position
    global final_position


    throwdice()
    print(f"You got an {dice_number}\n")
    time.sleep(1)
    position = position + dice_number
    final_position = 100 - position
    print(f"You have moved {dice_number} steps. You are only {final_position} steps away\n")
    return position
    if final_position == 100:
        print("You have won the game. Congratulations")
        pass
    else:
        pass

#ENEMY ENCOUNTER-----------------------------------------------------------------------

def enemy_encounter():
    
    #enemy stats
    time.sleep(2)
    enemy_health = np.random.randint(1,15)
    enemy_damage = np.random.randint(1,5)
 
    #function: attack the enemy with a weapon
    def weapon_attack():

        global character
    
        nonlocal enemy_health

        enemy_health = enemy_health - np.random.randint(character['weapon_damage']/2,character['weapon_damage'])
        print(f"You have attacked the enemy with your weapon. You have inflicted {character['weapon_damage']} of damage\n")
        return enemy_health
        time.sleep(3)


    def magic_attack():

        global character
    
        nonlocal enemy_health
    
        enemy_health = enemy_health - np.random.randint(character['magical_damage']/2,character['magical_damage'])
        print(f"You have attacked the enemy with magic. You have inflicted {character['magical_damage']} of damage\n")
        return enemy_health
        time.sleep(3)

    def defense():
        global character

        nonlocal enemy_damage
    
        enemy_damage_altered = enemy_damage / np.random.randint(2,5)
        character["health"] = character["health"] - enemy_damage_altered
        print(f"You have defended yourself from the attack. The damage you received is {enemy_damage_altered:.2f} Your health is {character['health']:.2f}\n")
        return character
        time.sleep(3)

    def enemy_attack():

        global character
    
        nonlocal enemy_damage
    
        character["health"] = character["health"] - enemy_damage
        print(f"The enemy has attacked you. The damage you received is {enemy_damage}. Your health is {character['health']}\n")
        return character
        time.sleep(3)   

    #battle starts

    len_enemies = len(enemies)

    enemy_selection = np.random.randint(0,len_enemies)

    

    print(f"YOU ARE BEING ATTACKED\nBY A {enemies[enemy_selection]}\n")


    #while you still have energy

    while character["health"] > 0:
    
        #different actions you can perform
    
        choice = input("Select an option\n1 for an attack\n2 for a magical attack\n3 for defense\n")
        if choice == "1":
            weapon_attack()
        if choice == "2":
            magic_attack()
        if choice == "3":
            defense()
            if character["health"] < 0:
                print("you have lost. Please restart")
                time.sleep(10)
                pass
            continue
            
        else:
            pass
        
        #if after your action, the enemy has 0 health, the battle ends with your victory

        if enemy_health < 0:
            print("You have won. Keep moving forward")
            time.sleep(2)
            return character["health"]
            pass
        
        #if the enemy still has energy, it will attack you
        enemy_attack()
        print(f"The enemy has attacked you. It has inflicted {enemy_damage} of damage")
        
        #if after the enemy attack, you have 0 health, you lose and the game ends

        if character["health"] < 0:
            print("you have lost. Please restart")
            time.sleep(10)
            pass


#OPEN A NEW WINDOW------------------------------------------------------------------------------------------------------

def create_new_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("Character Stats")

    # Add a label to display data
    label = tk.Label(new_window, text="Initial data: 0.00")
    label.pack()

    # Start updating the data
    update(label)

def update(label):
    
    global character
    
    # Generate new data (you can replace this with your own logic)


    # Update the label in the second window
    label.config(text=f"Your character: {character_name}\n Character Health: {character["health"]}\nCurrent Weapon: {character["weapon"]}\n Weapon Damage: {character["weapon_damage"]}\n Magical Damange: {character["magical_damage"]}")

    # Call the update function again after 1000 milliseconds (1 second)
    root.after(1000, update, label)



#///////////////////////////////////////////////////////////////////////////////////////


#Game start

print("Select character\nPress 1 for Barbarian or 2 for Mage")
character = input()
if character == "1":
    character = barbarian
    character_name = "Barbarian"
else:
   character = mage
   character_name = "Battlemage"

print(f"Greetings Traveller!.\n\nYou are a {character_name}. These are your initial stats\n\n")
print(f"-Health: {character['health']}\n-Weapon damage: {character['weapon_damage']}\n-Magical damage: {character['magical_damage']}\n-Initial Weapon: {character['weapon']}")
print("")
start_game = input("Do you want to throw the dice and start the game?\nPress enter to start")
time.sleep(2)

root = tk.Tk()
root.geometry("200x100")
create_new_window()


if start_game == "":
    while position < 100:
        time.sleep(2)
        move_forward()

        nrp_weapon = np.random.randint(1,4)
        if nrp_weapon < 4:
            find_weapon()

        nrp_encounter = np.random.randint(1,4)
        if nrp_encounter < 3:
            enemy_encounter()
        else:
            pass

else:
    pass
