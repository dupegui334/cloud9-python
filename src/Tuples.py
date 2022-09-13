#!/bin/bash

# TUPLES ARE NOT MUTABLES AND CAN'T CALL METHODS
fruits = ("Apples" , "Kiwi", "Orange")

print(type(fruits))# Print the type of data

# first_element = fruits(0) # Its nos going to work
# last_element = fruits(-1)
first_element = fruits[0] # It works
last_element = fruits[-1]

print(fruits) # Print the tuple


for i in fruits: # print the elements of the tuple with a for
    print (i)


for i in range(len(fruits)): # Another way to print elements of a tuple with a for
    print(fruits[i])

print(type(fruits))

print(len(fruits)) # lenght of the tuple

###################################################################
if "Apples" in fruits: # Check if an element "X" is in the tuple
    print("Yes, apple is in here")
else:
    print("No, it's not here")
    
if "Coco" not in fruits: # Check if an element "X" is not in the tuple
    print("No, coco is not here")
else:
    print("Nop, it's here")
    
# ######################### METHODS #################################
# ####INSERTING######
# fruits.append("grapes") # Append an item to the last position of the list
# fruits.insert(2, "Lemons") #Insert an element but moving the others
# fruits[2] = "Pineapple"# Insert an element but replacing the other
# ####INDEX##########
# index_apple = fruits.index("Apples") # Obtain the index of an item
# #####REMOVE########
# fruits.remove("Kiwi") # remove specific element with the name
# fruits.pop(0) # Delete element with the index
# fruits.pop() # Delete the last index
# del fruits[0]# Delete element with the index
# print(fruits)
# del fruits # Delete the list