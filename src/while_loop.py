#!/bin/bash

##############WHILE LOOP#############

# while True:#Infinite loop
#     print("Hey everyone")
    
count = 1
while count <= 100:#Finite loop
    
    if count % 2 == 0: # Print only the odds
        print(count)
        count += 1 # count = count + 1
    

count_2 = 1

while count_2 <= 100:#Finite loop
    
    if count_2 % 2 == 0: # Print only the evens
        count_2 += 1 # count = count + 1
        continue
        
    print(count_2)
    count_2 += 1 # count = count + 1