from MenuC import Menu

menu=Menu()

opcion=1;

while(opcion != 0):
    menu.MostrarMenu()
    opcion=int(input('Digite su opción: '))
    if(opcion==1):
        print('Agregar paciente')
        menu.AgregarPaciente(input('Ingrese la fecha de nacimiento del paciente: '), input('Ingrese el usuario del paciente: '),input('Ingrese la contraseña del paciente: '), input('Ingrese la cedula del paciente: '), input('Ingrese el nombre del paciente: '), input('Ingrese el apellido del paciente: '))
    elif((opcion==2)and(menu.getIngreso())):
        print('Consultar pacientes')
        menu.ConsultarPaciente()
    elif(opcion==3)and(menu.getIngreso()):
        print('Iniciar sesión')
        menu.IniciarSesion()
    elif(opcion==4)and(menu.getIngreso()):
        print('Cerrar sesión')
        menu.CerrarSesion()
    else:
        print('Opción incorrecta')