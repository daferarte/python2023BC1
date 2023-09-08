class Personas:

    def __init__(self, usuario, password, cedula, nombre, apellido):
        self.usuario = usuario
        self.password = password
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def getUsuario(self):
        return f'su usuario es: {self.usuario}'
    
    def getPassword(self):
        return f'su contrasena es: {self.password}'
    
    def getCedula(self):
        return self.cedula
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def setUsuario(self, usuario):
        self.usuario=usuario

    def setPassword(self, password):
        self.password=password
    
    def setCedula(self, cedula):
        self.cedula=cedula
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido=apellido

    def MostrarInformacion(self):
        return f'Su informacion personal es: {self.getUsuario()} {self.getPassword()}'