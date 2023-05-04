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
          for i in range(len(Invitado.lista_invitados)):
               if dni
          
          for d in range(len(Invitado.lista_dni_invitados)):
               if self.dni == Invitado.lista_dni_invitados[d]:
                    dni_ingresado = "si"
          for m in range(len(Invitado.lista_mail_invitados)):
               if self.mail == Invitado.lista_mail_invitados[m]:
                    mail_ingresado = "si"

          



          if nunca ingreso:
               print("Nunca ha ingresado todavía como Invitado. Debe registrarse.")
          else:
              
          
     
        pass
