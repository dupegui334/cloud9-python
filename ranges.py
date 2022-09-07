#!/bin/bash
#Ranges are not saved in memory
print(range(10))
#To save a Range in memory:
range_saved = list(range(5, 10))
print(type(range_saved))
print(range_saved)
range_saved = list(range(5, 10, 2))
print(range_saved)
range_saved = list(range(10, 1, -1))
print(range_saved)