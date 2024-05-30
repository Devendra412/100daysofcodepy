#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DAY 8
Caesar Cipher


# In[ ]:


print("Welcome To CAESAR CIPHER")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a=1
while a==1:
    to_do=input("Type 'encode' for encryption and 'decode' for decryption:")
    word=input("Type the message:\n").lower()
    shift=int(input("Enter the shift:\n"))
    
    
    def encrypt(p_text,shift_amt):
        cipher_word=""
        for char in p_text:
            pos=alphabets.index(char)
            newpos=pos+shift_amt
            new_char=alphabets[newpos]
            cipher_word+=new_char
        print("The encoded text is:",cipher_word)
        
    def decrypt(cipher_word,shift_amt):
        p_text=""
        for char in cipher_word:
            pos=alphabets.index(char)
            newpos=pos-shift_amt
            p_text+=alphabets[newpos]
        print("The decoded text is:",p_text) 
    
    if to_do=="encode":
        encrypt(p_text=word,shift_amt=shift)
    elif to_do=="decode":
        decrypt(cipher_word=word,shift_amt=shift)
        
    x=input("Do u want to continue? y/n?: ").lower()
    if x=="n":
        a=2
        print("Thankyou")
        


# In[ ]:





# In[ ]:




