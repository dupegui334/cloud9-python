#!/usr/bin/python3

def main():
    
    print('Hello, welcome to the coffee')
    name = input("What's your name?\n")
    menu = 'Coffee, tea or water?'
    orden = input('Hello ' + name + " what do you want to order? \n " + menu+ "\n")
    cantidad = int(input('Cuantas unidades deseas?\n'))
    precio = 4 # 4usd
    max_unid = 100
    
    if cantidad <= 100:
       print(name + ', El valor total de tu orden son $' + str(precio * cantidad)) 
    else:
        print('Ordenaste mas de las unidades permitidas: ' + str(max_unid))
    
    print('Vuelve pronto')
    
    
if __name__ == '__main__':
    main()