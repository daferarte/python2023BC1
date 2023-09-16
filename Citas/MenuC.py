from Paciente import Pacientes

class Menu:

    def __init__(self):
        print('Bienvenidos a mi aplicación de citas médicas')
        self.paciente=Pacientes('','','','','','')
        self.ingreso=False

    def getIngreso(self):
        return self.ingreso
    
    def setIngreso(self, ingreso):
        self.ingreso=ingreso

    def MostrarMenu(self):
        
        if(self.ingreso):
            print('2. Consultar pacientes')
            if(self.paciente.getAutenticado()):
                print('4. cerrar sesión')
            else:
                print('3. Iniciar sesión') 
        else:
            print('1. Agregar paciente')
            
        print('0. salir del sistema')
    
    def AgregarPaciente(self, fnacimiento, usuario, password, cedula, nombre, apellido):
        self.paciente.setUsuario(usuario)
        self.paciente.setPassword(password)
        self.paciente.setCedula(cedula)
        self.paciente.setNombre(nombre)
        self.paciente.setApellido(apellido)
        self.setIngreso(True)

    def ConsultarPaciente(self):
        print(self.paciente.MostrarInformacion())

    def IniciarSesion(self):
        print('Iniciar sesión')
        if(self.paciente.getAutenticado()):
            print('Ya existe una sesión iniciada')
        else:
            if(self.paciente.IniciarSesion(input('Ingrese su usuario: '),input('Ingrese su contraseña: '))):
                print('Inicio de sesión exitoso')
            else:
                print('Usuario y contraseña incorrecta')
    
    def CerrarSesion(self):
        print('Cerrar sesión')
        if(self.paciente.getAutenticado()):
            self.paciente.setAutenticado(False)
            print('Hasta pronto')
        else:
            print('Aun no inicia sesión')