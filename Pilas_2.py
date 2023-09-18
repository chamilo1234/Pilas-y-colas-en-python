class Pila:
    #crear una pila
    def __init__(self):
        self.Dato = []
        
    #verifica si la pila esta vacia o tiene datos y arroja una respuesta de verdad o falso
    def pilaVacia(self):
        return self.Dato == []
    
    #inserte el dato de la pila
    def InsertaDato(self, Dato):
        self.Dato.append(Dato)
        
    #desapilar ultimo elemento
    def Desapilar(self):
        return self.Dato.pop()
    
    #muestra el ultimo dato apilado
    def leerUltimo(self):
        return self.Dato[len(self.Dato)-1]
    
    #muestra el tamaño  que tiene la pila
    def tamano(self):
         return len(self.Dato)
    #muestra los elementos que contiene la pila
    def mostrar (self):
        print(self.Dato)
    #para limpiar la pila y empezar nuevamente
    def limpiar (self):
        del self.Dato


#Programa Principal
print("DESARROLLADO POR JOSE ARMANDO BENAVIDES CANCHALA Y JUAN CAMILO MORALES LOPEZ.")
print()
print("Bienvenido este es un programa impementar el funcionamiento de una Pila.")
print()
print(input("Para Crear la pila oprima Enter "))

p=Pila()


#**************************
#creamos una funcion llamada menu para llamar las funciones de pila
def menu():
    print ("Selecciona una opción.")
    print()
    print ("1: Verifica si la pila esta  vacia.")
    print ("2: Insertar dato a la pila.")
    print ("3: desapilar ultimo elemento.")
    print ("4: ver ultimo elemento.")
    print ("5: tamaño de datos que contiene la pila.")
    print ("6: mostrar los datos de la pila.")
    print ("7: limpiar completa la pila.")
    print ("8: salir.")
 
#es un ciclo que repite el llamado a las opciones segun la condicion de salida
while True:
    # Mostramos el menu
    menu()
    # solicitamos que elija una opción el usuario
    print()
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=="1":
        print ("")
        input("Has pulsado la opción 1...\npara verificar si la pila esta vacia pulsa una tecla para continuar")
        print()
        if  p.pilaVacia()==True:
            print("la pila esta vacia.")
        else:
            print("la pila tiene datos.")
        print()

    elif opcionMenu=="2":
        print ("")
        input("Has pulsado la opción 2...\npara insertar datos pulsa una tecla para continuar")
        dato=input("Ingrese un dato: ")
        p.InsertaDato(dato)

    elif opcionMenu=="3":
        print ("")
        input("Has pulsado la opción 3...\npara desapilar un dato pulsa una tecla para continuar")
        print()
        print("El Dato desapilado es: ",p.Desapilar())
        print()

    elif opcionMenu=="4":
        print()
        input("Has pulsado la opción 4...\npara ver el ultimo elemento apilado pulsa una tecla para continuar")
        print(p.leerUltimo())

    elif opcionMenu=="5":
        print()
        input("Has pulsado la opción 5...\npara ver el tamaño de la pila pulsa una tecla para continuar")
        print(p.tamano())

    elif opcionMenu=="6":
        print()
        input("Has pulsado la opción 6...\npara mostrar los elementos de la pila pulsa una tecla para continuar")
        print(p.mostrar())

    elif opcionMenu=="7":
        print()
        input("Has pulsado la opción 7...\npara limpiar la pila pulsa una tecla para continuar")
        p.limpiar()

    elif opcionMenu=="8":
        exit()
        

    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npara volver al menu inicial pulsa una tecla para continuar")


    


#print(p.pilaVacia()) #1
#p.InsertaDato(4)
#p.InsertaDato('perro')
#print(p.leerUltimo())#2
#p.InsertaDato(568)
#print(p.tamano())
#print(p.pilaVacia())
#p.InsertaDato(8.4)
#print(p.Desapilar())
#print(p.Desapilar())
#print(p.tamano())
