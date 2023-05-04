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
               for d in range(len(Invitado.lista_dni_invitados)):
                    if self.dni == Invitado.lista_dni_invitados[d]:
                         if self.email == Invitado.lista_mail_invitados[d]:
                              print("Perfecto. Puede actualizar sus datos.")
                              entrar = "si"
                              while entrar == "si":
                                   dato = int(input("""Ingrese el nro. correspondiente para el dato que desea actualizar.
                                   1- Nombre
                                   2- Apellido
                                   3- DNI
                                   4- email
                                   """))
                              
               print("Para el usuario invitado no coinciden ese dni y ese mail.")


          
     #      cuando pida los datos para modificarlos
     #      while dni in Usuario.lista_dni and dni in Invitado.lista_dni_invitados:


          



     #      if nunca ingreso:
     #           print("Nunca ha ingresado todavía como Invitado. Debe registrarse.")
     #      else:
     #           pass
              
          
     
     #    pass
