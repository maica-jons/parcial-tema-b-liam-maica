class Usuario():

    lista_usuarios = []
    lista_dni = []
    lista_mail = []
    lista_nom_usuarios = []

    def __init__(self, nom_usuario, contra, nombre, apellido, dni, mail):
        self.nom_usuario = nom_usuario
        self.contra = contra
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

    def __str__(self):
        return("Mi nombre de usuario es {}.Me llamo {} {}, mi DNI es {}, mi mail es {} y mi contraseña es {}.".format(self.nom_usuario,self.apellido,self.nombre,self.dni,self.mail,self.contra))


    # def cambiar_contra(self,nueva):
    #     self.contra = nueva
    #     print("Se cambió exitosamente la contraseña.")

    def cambiar_contra(self, esta):
        contrasena = input("Primero ingrese su contraseña vieja: ")
        try:
            if contrasena != self.contra:
                raise ValueError
            contra_nueva = input("Ingrese su nueva contraseña: ")
            self.contra = contra_nueva
            esta = "Sí"
            print("Se cambió exitosamente la contraseña.")
        except:
            print("La contraseña es incorrecta.")
        return esta