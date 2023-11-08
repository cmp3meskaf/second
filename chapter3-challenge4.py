# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:21:42 2023

@author: CMP3MESKAF
"""



import random

high = int(input("What is the highest number I should guess to? "))
low = int(input("What is the lowest number I should guess to? "))

# while guess is incorrect:
guessed_incorrectly = True

while guessed_incorrectly:
# edit the upper and lower limits of the random number gen.
    guess = random.randint(low, high)
    print("\nMy guess is ", guess)
    is_comp_correct = input("\nIs my number correct? Y or N? ")
    if is_comp_correct.title() == 'Y':
        print ("hoooray")