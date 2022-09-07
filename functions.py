#!/bin/bash
def hello_world():
    print('Hi there')

def suma(a,b):
    result = a + b
    print(a+b)

def product(a,b):
    result = a * b
    return result
    
def main():
    
    hello_world()
    suma(1,2)
    print(product(10,2))
    
if __name__ == '__main__':
    main()