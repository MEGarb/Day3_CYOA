print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.  Your goal is to leave with the the treasure.")
fork = input("There is a fork in the road.  Do you want to go 'left' or 'right'?  ")
if fork == "right":
    river = input("You have come to a river. Would you like to 'swim' or 'wait' for a boat?  ")
    if river == "wait":
        print("You have accepted a boat ride from a creepy old man.  ")
        door = input("Before you lies a 'green' door, a 'blue' door and a 'red' door. \nWhich do you choose?  ")
        if door == "green":
            print("You have found the greatest treasure of all. You are still alive. You are still broke, but alive.")
        elif door == "blue":
            print("You open the door and fall down a mineshaft. Good news is that you are relativly \nunhurt and now the owner of a sphire mine. The bad news is you need to find a way out.")
        elif door == "red":
            print("The door was red because it was on fire. Like this whole room is on fire. \nYou should have seen that. You die.")
        else:
            print("Unexpected input.")
    elif river == "swim":
        print("Why did you do that? You know you cant swim. You drown until you die.")
    else:
        print("Unexpected input.")
elif fork == "left":
    print("You walked into a bog you did not see because of how dark it is.  You are dead.")
else:
    print("Unexpected input.")