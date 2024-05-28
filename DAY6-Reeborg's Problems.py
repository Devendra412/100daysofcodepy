#!/usr/bin/env python
# coding: utf-8

# DAY 7
# Reeborg's World Path Problems
# 
# This is a Reeborg world problem.
# Go to:  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# In[ ]:


#HURDLE PROBLEM
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
           
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    else:
        turn_left()

#MAZE PROBLEM
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    else:
        turn_left()

