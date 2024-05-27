#!/usr/bin/env python
# coding: utf-8

# DAY 5
# PASSWORD GENERATOR

# In[1]:


import random
alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '&', '*','_','?']       #prerequisites

print("Welcome to the PASSWORD GENERATOR!")
req_alpha=int(input("Enter the number of letters you want in password: "))
req_num=int(input("Enter number of numericals you want in password: "))  #input
req_sym=int(input("Enter the number of symbols you want in password: "))

pass_list=[]                       #empty_list
for i in range(1,req_alpha+1):          
    pass_list.append(random.choice(alphabets))    #randomalpha

for i in range(1,req_num+1):
    pass_list.append(random.choice(numbers))      #randomnum
    
for i in range(1,req_sym+1):
    pass_list.append(random.choice(symbols))      #randomsymbols
    
random.shuffle(pass_list)                         #shuffling
password=""                                       #empty_string
for i in pass_list:
    password+=i                                   #coverting_list-string

print("The password for you is: ",password)
print("Thankyou!!")


# In[ ]:




