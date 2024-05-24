#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DAY:2  
TIP CALCULATOR ON BILL


# In[1]:


'''Welcome message'''
print("Welcome to the TIP CALCULATOR")

'''input'''
bill=float(input("Enter the total bill: $"))
percent=float(input("Enter the percent of tip you want to give: "))

'''calculation of total bill'''
totalbill= (bill*(percent/100))+bill
splitfriends=int(input("Enter the number of friends to split the bill: "))

'''splitting among friends, rounding to 2 decimals'''
totalbill=round((totalbill/splitfriends),2)
print("Each one of you has to pay $",totalbill)


# In[ ]:




