#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DAY-3
TREASURE ISLAND GAME


# In[2]:


print('''*******************************************************************************
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
print("Welcome to Treasure Island! It is a Game Of Luck and your mission is to find the Treasure.")
ch1=input("You're at a crossroad. Do you want to go 'left' or 'right' ?: \n ").lower()
if(ch1=="left"):
    ch2=input("You are standing at the bank of a lake and there is an island in it. Do you want to 'wait' for a boat or 'swim' ?: \n ").lower()
    if(ch2=="wait"):
        ch3=input("You have arrived at the island. You see three doors of Red, Yellow and Blue colours. What door do you choose from 'red' or 'blue' or 'yellow' ?: \n ").lower()
        if (ch3=="red"):
            print("You died in fire.\n GAME OVER")
        elif (ch3=="blue"):
            print("You have found the Treasure.\n CONGRATULATIONS!!")
        else:
            print("You were eaten by Beasts.\n GAME OVER")
    else:
        print("You were eaten by an Alligator.\n GAME OVER")
else:
    print("You died of unknown reasons.\n GAME OVER")


# In[ ]:




