#!/bin/bash

# LISTS ARE MUTABLES AND CAN CALL METHODS
fruits = ["Apples" , "Kiwi", "Orange"]

print(type(fruits))# Print the type of data

first_element = fruits[0]
last_element = fruits[-1]

print(fruits) # Print the list

for i in fruits: # print the elements of the list with a for
    print (i)


for i in range(len(fruits)): # Another way to print elements of a list with a for
    print(fruits[i])
    
print(len(fruits)) # lenght of the list

###################################################################
if "Apples" in fruits: # Check if an element "X" is in the list
    print("Yes, apple is in here")
else:
    print("No, it's not here")
    
if "Coco" not in fruits: # Check if an element "X" is not in the list
    print("No, coco is not here")
else:
    print("Nop, it's here")
    
######################### METHODS #################################
####INSERTING######
fruits.append("grapes") # Append an item to the last position of the list
fruits.insert(2, "Lemons") #Insert an element but moving the others
fruits[2] = "Pineapple"# Insert an element but replacing the other
####INDEX##########
index_apple = fruits.index("Apples") # Obtain the index of an item
#####REMOVE########
fruits.remove("Kiwi") # remove specific element with the name
fruits.pop(0) # Delete element with the index
fruits.pop() # Delete the last index
del fruits[0]# Delete element with the index
print(fruits)
del fruits # Delete the list
