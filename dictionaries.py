#!/bin/bash

stock = { "Apples": 100, "Kiwi": 50, "lemons": 10} 
print(stock["Apples"]) # Consulting the value of a key in the dictionary

######### CONSULTING VALUE ############
print(stock.get("apple")) # its case sensitive, if the key doesn't exist there is not going to be error but a none answer
values_stock = stock.values()
print(values_stock)

######### CONSULTING KEYS ############
keys_stock = stock.keys()
print(keys_stock)

########## ASSIGN ##############
stock["Apples"] = 200 # Assign value to a key of the dictionary
stock["Coco"] = 700 # Assign new key and value to the dictionary if the key doesnt exist
print(stock)

########### REMOVING KEYS ############
del stock["Kiwi"]
stock.pop("Coco")
print(stock)
del stock # delete the dictionary

