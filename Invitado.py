from Usuario import Usuario

class Invitado():

     lista_invitados = []
     lista_dni_invitados = []
     lista_mail_invitados = []

     def __init__(self, nombre, apellido, dni, email, cantidad_ingresos =0):  
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.cantidad_ingresos = cantidad_ingresos
     
    #  def __str__(self):
    #     return (pass)
    

     def actualizar_datos(self):

        lista_dni_usuario = Usuario.lista_dni
        lista_mails_usuario = Usuario.lista_mail

        if (len(Invitado.lista_dni_invitados) == 0) or (len(Invitado.lista_mail_invitados) == 0):
            print("No se han creado usuarios invitados todavía. Para crear uno, seleccione la opción correspondiente en el menú.")
          
        elif (self.dni not in Invitado.lista_dni_invitados) or (self.email not in Invitado.lista_mail_invitados):
            print("Los datos del usuario fueron ingresados incorrectamente.")
          
        elif (self.dni in Invitado.lista_dni_invitados):
            for d in range(len(Invitado.lista_invitados)):
                if self.dni == Invitado.lista_invitados[d].dni and self.email == Invitado.lista_invitados[d].email:
                    print("Perfecto. Puede actualizar sus datos.")
                    salir = "no"
                    while salir != "si":
                        try:
                            dato = int(input("""Ingrese el nro. correspondiente para el dato que desea actualizar.
                            1- Nombre
                            2- Apellido
                            3- DNI
                            4- email
                            """))
                            while dato not in [1,2,3,4,5]:
                                    dato = int(input("""Ingrese el nro. correspondiente para el dato que desea actualizar.
                                    1- Nombre
                                    2- Apellido
                                    3- email
                                    4- DNI
                                    """))
                            if dato == 1:
                                    nombre_nuevo = input("Ingrese el nuevo nombre: ")
                                    self.nombre = nombre_nuevo
                                    print(f"El nombre fue actualizado con éxito a {self.nombre}")
                            elif dato == 2:
                                    apellido_nuevo = input("Ingrese el nuevo apellido: ")
                                    self.apellido = apellido_nuevo
                                    print(f"El apellido fue actualizado con éxito a {self.apellido}")
                            elif dato == 3:
                                    email_nuevo = input("Ingrese el nuevo email: ")
                                    while email_nuevo in lista_mails_usuario or email_nuevo in Invitado.lista_mail_invitados:
                                        email_nuevo = input("Ese mail ya fue usado por otro usuario. Debe ingresar otro: ")
                                    if self.email in Invitado.lista_mail_invitados:
                                        Invitado.lista_mail_invitados.remove(self.email)
                                        self.email = email_nuevo
                                        Invitado.lista_mail_invitados.append(self.email)
                                    elif self.email in lista_mails_usuario:
                                        lista_mails_usuario.remove(self.email)
                                        self.email = email_nuevo
                                        lista_mails_usuario.append(self.email)
                                    print(f"El email fue actualizado con éxito a {self.email}")
                            elif dato == 4:
                                    dni_nuevo = input("Ingrese el nuevo DNI: ")
                                    while dni_nuevo in lista_dni_usuario or dni_nuevo in Invitado.lista_dni_invitados:
                                        dni_nuevo = input("Ese DNI ya está registrado. No pueden haber 2 usuarios con mismo DNI. Elija otro: ")
                                    if self.dni in Invitado.lista_dni_invitados:
                                        Invitado.lista_dni_invitados.remove(self.dni)
                                        self.dni = dni_nuevo
                                        Invitado.lista_dni_invitados.append(self.dni)
                                    elif self.dni in lista_dni_usuario:
                                        lista_dni_usuario.remove(self.dni)
                                        self.dni = dni_nuevo
                                        lista_dni_usuario.append(self.dni)
                                    self.dni = dni_nuevo
                                    print(f"El DNI fue actualizado con éxito a {self.dni}")
                            elif dato == 5:
                                break    
                                    
                            
                            
                        except:
                            print("Ingrese UN NUMERO.")
                         
                         #Un usuario con el mismo dni no se puede registrar con diferentes mails. Tampocopodrá registrarse más de un usuario con un mismo mail.
                         # #Recuerde que debe llevar el registro delcontador de veces que ha ingresado como usuario invitado


