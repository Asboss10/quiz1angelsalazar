def contraseña():
    contraseña = input("ingrese su contraseña :")
    upper=0
    space=0
    num=0
    largo = 0
    espacio = " "

    if contraseña.isupper()==True:
        upper=True
    if espacio in contraseña:
        space =True

    while 1<=len(contraseña)<=8:
        if upper==True and space==False:
            print("su contraseña {} ha sido creada con exito!".format(contraseña))
            break
        else:
            print("Disculpe la contraseña no cumple nuestros requisitos corra denuevo el programa")
            break

            

contraseña()

       
