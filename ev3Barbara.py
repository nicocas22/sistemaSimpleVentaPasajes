# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 19:17:02 2022

@author: Nicog
"""
global pasajeros

pasajeros = list()


asientos = [["1", "2", "3", "4", "5", "6"],
            ["7", "8", "9", "10", "11", "12"],
            ["13", "14", "15", "16", "17", "18"],
            ["19", "20", "21", "22", "23", "24"],
            ["25", "26", "27", "28", "29", "30"],
            ['--------------------------------'],
            ["31", "32", "33", "34", "35", "36"],
            ["37","38","39","40","41","42"]]

class pasajero:
    rut = 0
    nombre = ""
    celular = 0
    banco = ""
    asiento = ""
    total = 0
    indexAsiento = 0

class funciones:
    def mostrarAsientos():
        for i in asientos:
            print(i)
    def bancos():
        banco = ['banco Duoc', 'banco Estado' , 'banco Chile']
        suBanco = input('''Elija una opcion de su banco: 
                        1.- Banco Duoc
                        2.- Banco Estado
                        3.- Banco Chile
                        ''' )
        contador = 0
        for nombreBanco in banco:
            contador = contador + 1
            if int(contador) == int(suBanco):
                return nombreBanco
           
    def comprarAsiento():
        pasajeroInstance = pasajero()
        pasajeroInstance.rut = input("Ingrese Rut Del Pasejeros: ")
        pasajeroInstance.nombre = input("Ingrese su nombre: ")
        pasajeroInstance.celular = input("Ingrese Su Telefono: ")
        pasajeroInstance.banco = funciones.bancos()
        pasajeroInstance.asiento = input("Ingrese Su numero: ")
        asient = pasajeroInstance.asiento
        bank = pasajeroInstance.banco
        if int(asient) > 0 and int(asient) < 31:
            if bank == "banco Duoc":
                print("Su asiento es Normal su precion a pagar es de 78900 - 15% Por ser Banco Duoc Felicidades")
                restaPorcentaje = (78900 *15) / 100
                pasajeroInstance.total = 78900 - restaPorcentaje     
            else:    
                print("Su asiento es Normal su precion a pagar es de 78900")
                pasajeroInstance.total = 78900
        else: 
            if bank == "banco Duoc":
                print("Su asiento es VIP su precio a pagar es de 240000 - 15% Por ser Banco Duoc Felicidades")
                restaPorcentaje = (240000 *15) / 100
                pasajeroInstance.total = 240000 - restaPorcentaje     
            else:  
                print("Su asiento es VIP su precio a pagar es de 240000")
                pasajeroInstance.total = 240000
        
        for fila in asientos:
            contadorDeAsiento = 0
            for asiento in fila:
                if asiento == asient:
                    fila[contadorDeAsiento] = "x"
                    pasajeroInstance.indexAsiento = contadorDeAsiento
                    return pasajeros.append(pasajeroInstance)
                contadorDeAsiento = contadorDeAsiento+1
                
    def anularPasaje():
        #Pedir el numero de asiento
        numAsiento = int(input("Numero de Pasaje a anular"))
        print(numAsiento)
        for pasajero in pasajeros:
            print(pasajero.rut)                  
            #Aqui debo dejar la restauracion del pasaje
            pasajeros.remove(pasajero)        
        return print("Se elimino el registro del asiento ", numAsiento)
             
    def ModificarUsuario():
        rut = int(input("Ingrese Rut: "))
        numAsiento = int(input("Numero de Pasaje"))
        for i in pasajeros:
            pasajer =pasajero()
            print(i.asiento)
            print(numAsiento)
            print(rut)
            print(i.rut)
            if int(i.rut) == rut and int(i.asiento)== numAsiento:
                print("Entra por aca ?")
                while True:
                    print('''MENÚ
                          1.-Modificar Nombre
                          2.-Modificar Celular
                          3.-Salir''')
                    opcion = int(input("ingrese su opcion : "))
                    if opcion == 1:
                        print("has seleccionado modificar nombre")
                        i.nombre = input("ingrese su nuevo nombre: ")
                        break
                    elif opcion == 2:
                        print("has eleccionado Modificar celular")
                        i.celular = input("ingrese su nuevo numero: ")
                        break
                    elif opcion == 3:
                        print("Volver")
                        break
    def listaPasajeros():
        for pasa in pasajeros:
            print(pasa.rut)
            print(pasa.nombre)
            print(pasa.celular)
            print(pasa.numAsiento)
            print(pasa.banco)
        
                

def menu():  # Esta es la funcion menu una funcion se define con def elnombre(): y los parentecis pegados al nombre cerrando con :
    print('''MENÚ
          1.-Ver Asientos Disponibles
          2.-Comprar Asiento
          3.-Anular Vuelo
          4.-Modificar Datos Pasajeros
          5.-SALIR''')
    opcion = int(input("ingrese su opcion : "))
    while True:

        if opcion == 1:
            print("has seleccionado Mostrar Asientos Disponibles")
            funciones.mostrarAsientos()

        elif opcion == 2:
            print("has eleccionado Comprar asiento")
            funciones.comprarAsiento()

        elif opcion == 3:
            print("has seleccionado Anular Pasaje")
            funciones.anularPasaje()
        elif opcion == 4:
            funciones.ModificarUsuario()
        elif opcion == 5:
            funciones.listaPasajeros()
        else:
           print("Opcion invalida")

        print('''MENÚ
             1.-Ver Asientos Disponibles
             2.-Comprar Asiento
             3.-Anular Vuelo
             4.-Modificar Datos Pasajeros
             5.-SALIR''')
        opcion=int(input("ingrese su opcion : "))
    


menu()

