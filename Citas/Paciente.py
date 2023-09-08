from Personas import Personas

class Pacientes(Personas):

    def __init__ (self, fNacimiento, usuario, password, cedula, nombre, apellido):
        super().__init__(usuario, password, cedula, nombre, apellido)
        self.fNacimiento= fNacimiento

    def getFNacimiento (self):
        return f'Su fecha de nacimiento es: {self.fNacimiento}'
    
    def MostrarInformacion(self):
        return f'{super().MostrarInformacion()} {self.getFNacimiento()}'