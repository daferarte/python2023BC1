
print('Bienvenidos a mi aplicación de citas médicas')

opcion=-1

while(opcion != 0):
    print('1. Agregar paciente')
    print('2. Consultar pacientes')
    print('3. Iniciar sesión')
    print('4. cerrar sesión')
    print('0. salir del sistema')

    opcion=int(input('Digite su opción: '))

    if(opcion==1):
        print('Agregar paciente')
    elif(opcion==2):
        print('Consultar pacientes')
    elif(opcion==3):
        print('Iniciar sesión')
    elif(opcion==4):
        print('Cerrar sesión')