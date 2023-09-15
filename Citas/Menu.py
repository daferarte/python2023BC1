from Paciente import Pacientes
print('Bienvenidos a mi aplicación de citas médicas')

opcion=-1
paciente=''

while(opcion != 0):
    print('1. Agregar paciente')
    print('2. Consultar pacientes')
    print('3. Iniciar sesión')
    print('4. cerrar sesión')
    print('0. salir del sistema')

    opcion=int(input('Digite su opción: '))

    if(opcion==1):
        print('Agregar paciente')
        paciente=Pacientes(input('Ingrese la fecha de nacimiento del paciente: '), input('Ingrese el usuario del paciente: '),input('Ingrese la contraseña del paciente: '), input('Ingrese la cedula del paciente: '), input('Ingrese el nombre del paciente: '), input('Ingrese el apellido del paciente: '))
    elif(opcion==2):
        print('Consultar pacientes')
        print(paciente.MostrarInformacion())
    elif(opcion==3):
        print('Iniciar sesión')
        if(paciente.getAutenticado()):
            print('Ya existe una sesión iniciada')
        else:
            if(paciente.IniciarSesion(input('Ingrese su usuario: '),input('Ingrese su contraseña: '))):
                print('Inicio de sesión exitoso')
            else:
                print('Usuario y contraseña incorrecta')
    elif(opcion==4):
        print('Cerrar sesión')
        if(paciente.getAutenticado()):
            paciente.setAutenticado(False)
            print('Hasta pronto')
        else:
            print('Aun no inicia sesión')
    else:
        print('Opción incorrecta')