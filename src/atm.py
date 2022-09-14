def main():
    continuar = True
    total = 1000.0
    
    while continuar == True:
        opcion = input('''Bienvenido al banco BBVA, seleccione entre las opciones:
        1. Consignar
        2. Retirar
        3. Salir
    ''')
        if opcion == '1':
            consignar = float(input('Ingrese valor a consignar\n'))
            
            if consignar <= total:
                total -= consignar
                cuenta = input('ingrese numero de cuenta\n')
                print(f'Se ha consignado ${consignar}, a la cuenta {cuenta}, le quedan ${total}')
            
            else:
                print(f'Saldo insuficiente, solo tiene ${total}')
                
        elif opcion == '2':
            retirar = float(input('Ingrese valor a retirar\n'))
            if retirar <= total:
                total -= retirar
                print(f'Se ha retirado ${retirar}, le quedan ${total}')
            else:
                print(f'Saldo insuficiente, solo tiene ${total}')
        
        elif opcion == '3':
            continuar = False
            
        else:
            print('Seleccione opcion correcta')
            
    print('Hasta luego')
    quit()
    
if __name__ == '__main__':
    main()