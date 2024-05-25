#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DAY 4
ROCK-PAPER-SCISSORS GAME


# In[1]:


import random

'''ASCII images of rock, paper and scissors'''
rock='''Rock
_______
---'   ____)
      (_____)
      (_____)                              
      (____)
---.__(___)
'''
paper='''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissors]                  #adding in list
print("Welcome to Rock-Paper-Scissors Game!")
a=1                 
while a==1:         #for recurring option to play
        ch=int(input("0-Rock; 1-Paper; 2-Scissors. Enter your choice from 0,1,2: "))
        if ch>2 or ch<0:                  #for out of range cases
            print("Enter valid number")
        else:
            print("Your choice: ")
            print(images[ch])
            comp=random.randint(0,2)      #random generator 
            print("Computer's choice: ")
            print(images[comp])
            
            if ch==0 and comp==2:
                print("You won!!")
            elif comp==0 and ch==2:
                print("You Lost!")       #defining cases and their outcomes
            elif comp>ch:
                print("You Lose!")
            elif comp==ch:
                print("It's a Draw!!!")
            else:
                print("You Won!!")
                
        x=input("Want to continue playing? Type Y for YES; N for NO: ").lower()
        if x=='n':
            print("Thankyou")
            a=0                         #exiting the game 
        elif x!='y' and x!='n':
            print("Enter correctly\n")
        else:
            continue
        
                


# In[ ]:




