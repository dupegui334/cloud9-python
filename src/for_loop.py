#!/bin/bash

########### FOR LOOP WITH LISTS #################

fruits = ["Apples" , "Kiwi", "Orange"]

print(fruits) # Print the list

for i in fruits: # print the elements of the list with a for
    print (i)

for i in range(len(fruits)): # Another way to print elements of a list with a for
    print(fruits[i])
    
print(range(len(fruits)))

for i in fruits: # Another way to print elements of a list with a for
    print(fruits)
    
    if i == "Apples": # i is going to have the value of the item
        print('Here we have apples!')

list_dots = [(1, 2), (3, 4), (5, 0)]

##########TUPLES INSIDE OF LISTS##############

for x,y in list_dots:
    print("x:" + str(x) + " y:" + str(y))
        
########### FOR LOOP WITH DICTIONARIES #################
stock = { "Apples": 100, "Kiwi": 50, "lemons": 10} 
for keys in stock:
    print(keys)
    
for item,qty in stock.items():
    print("Item: " + item)
    print("qty: " + str(qty))

########## FOR LOOP WITH STRINGS #############
for letter in "my name":
    print(letter)