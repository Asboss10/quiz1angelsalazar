import sys

BaseDedatos = {}
BaseDedatos2 = {}

def agregar():
    boleto = 40
    cedula = 0
    edad = 0
    continuar = 1
    continuar2 = 1
    nombre = input("Porfavor escriba su nombre completo: ")
    
    while continuar == 1:
        edad = int(input("Ingrese su edad"))

        if edad > 0: 
            continuar = 2
        else:
            print("Porfavor ingrese una edad valida") 


    while continuar2 == 1:

        cedula = int(input("Ingrese sucedula"))
        if cedula > 99:
            continuar2 = 2
        else:
            print("Porfavor ingrese una cedula mayor de 2 digitos o una cedula valida")

    cedula = str(cedula)

    cedula3 = cedula[-3]
    cedula2 = cedula[-2]
    cedula1 = cedula[-1]

    if edad > 0:
        if edad > 55 :
            if cedula3 < cedula2:
                if cedula2 < cedula1:
                    Descuento1 = 40 * 0.40
                    descuento2 = 40 * 0.30
                    DescuentoTotal = descuento2 + Descuento1
                    boleto2 = boleto - DescuentoTotal

                    print("Hola{}Su precio total es: {}, Su precio sin descuento es:{}, y el total de descuento es:{}".format(nombre,boleto2,boleto,DescuentoTotal))

                    BaseDedatos[nombre] = boleto2
                    BaseDedatos2[nombre] = nombre

                    menu()

                else:

                    Descuento1 = 40 * 0.40
                    descuento2 = 0
                    DescuentoTotal = descuento2 + Descuento1
                    boleto2 = boleto - DescuentoTotal

                    print("Hola{}Su precio total es: {}, Su precio sin descuento es:{}, y el total de descuento es:{}".format(nombre,boleto2,boleto,DescuentoTotal))

                    BaseDedatos[nombre] = boleto2
                    BaseDedatos2[nombre] = nombre

                    menu()

            else:

                    Descuento1 = 40 * 0.40
                    descuento2 = 0
                    DescuentoTotal = descuento2 + Descuento1
                    boleto2 = boleto - DescuentoTotal  

                    print("Hola{}Su precio total es: {}, Su precio sin descuento es:{}, y el total de descuento es:{}".format(nombre,boleto2,boleto,DescuentoTotal))

                    BaseDedatos[nombre] = boleto2
                    BaseDedatos2[nombre] = nombre

                    menu()  

        else:
            if cedula3 < cedula2:
                if cedula2 < cedula1:
                    Descuento1 = 0
                    descuento2 = 40 * 0.30
                    DescuentoTotal = descuento2 + Descuento1
                    boleto2 = boleto - DescuentoTotal

                    print("Hola{}Su precio total es: {}, Su precio sin descuento es:{}, y el total de descuento es:{}".format(nombre,boleto2,boleto,DescuentoTotal))

                    BaseDedatos[nombre] = boleto2
                    BaseDedatos2[nombre] = nombre

                    menu()

                else:
                    Descuento1 = 0
                    descuento2 = 0
                    DescuentoTotal = descuento2 + Descuento1
                    boleto2 = boleto - DescuentoTotal 

                    print("Hola{}Su precio total es: {}, Su precio sin descuento es:{}, y el total de descuento es:{}".format(nombre,boleto2,boleto,DescuentoTotal))

                    BaseDedatos[nombre] = boleto2
                    BaseDedatos2[nombre] = nombre

                    menu()     

            else:
                    Descuento1 = 0
                    descuento2 = 0
                    DescuentoTotal = descuento2 + Descuento1
                    boleto2 = boleto - DescuentoTotal  

                    print("Hola{}Su precio total es: {}, Su precio sin descuento es:{}, y el total de descuento es:{}".format(nombre,boleto2,boleto,DescuentoTotal))

                    BaseDedatos[nombre] = boleto2
                    BaseDedatos2[nombre] = nombre

                    menu()    

    else:
        print("Porfavor ingrese una edad valida")
        agregar()        


def consultar():
    Print("Personas registradas por ahora:")

    for i in BaseDedatos:
        print("Nombre: {}, Deuda: {}".format(BaseDedatos2[i],BaseDedatos[i]))
        menu() 

def eliminar():

    nombre = input("Porfavor escriba el nombre del cliente que desea eliminar de la base de datos")

    try:
        del BaseDedatos[nombre]
        del BaseDedatos2[nombre]
        print("Se elimino el usuario de la base de datos")
        menu() 
    except:
        print("No existe ese usuario en la base de datos volveras al menu")
        menu() 

def menu():

    print("Escriba 1 Si desea agregar un cliente, Escriba 2, si desea eliminar un cliente, escriba 3 si desea eliminar un cliente")

    numero = int(input(""))

    if numero == 1:
        agregar()
    elif numero == 2:
        eliminar()
    elif numero == 3:
        consultar()
    else:
        print("Porfavor ingrese un numero valido")


menu()       





        




