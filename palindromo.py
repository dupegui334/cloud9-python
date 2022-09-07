#!/bin/bash

def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    #print(palabra)
    palabra_invertida = palabra[::-1]#from the beginning to the end of the str in negative steps
    #print(palabra_invertida)
    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input('Ingrese la palabra:\n')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    main()