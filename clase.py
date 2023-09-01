class Animales:
    color=''
    raza=''
    peso=0
    sexo=''
    nombre=''
    edad=0

    def __init__(self, color, raza, peso, sexo, nombre, edad):
        self.color = color
        self.raza = raza
        self.peso = peso
        self.sexo = sexo
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f'estoy comiendo')

    def caminar(self):
        return 'estoy caminando'
    
    def Dormir(self):
        return f'soy {self.nombre} y estoy durmiendo'
    
    def Jugar(self):
        return f'soy {self.nombre} tengo {self.edad} y estoy jugando'

class Perro(Animales):

    caninos = False
    olfato = True

    def __init__(self, color, raza, peso, sexo, nombre, edad, caninos, olfato=True):
        super().__init__(color, raza, peso, sexo, nombre, edad)
        self.caninos=caninos
        self.olfato= olfato

    def ladrar(self):
        return f'estoy ladrando'
    
    def aullar(self):
        return f'estoy aullando'
    
    def morder(self):
        if self.caninos:
            return f' soy {super().nombre} y estoy mordiendo'
        else:
            return f'no puedo morder'
    
    def caminar(self):
        return f'estoy caminando'

tobi = Perro('dorado', 'golden retriever', 20, 'H', 'tobi', 5, True)
cobi = Perro('dorado', 'golden retriever', 20, 'H', 'cobi', 5, False, False)

print(tobi.morder())
print(cobi.morder())


# pelusa= Animales('dorado', 'golden retriever', 20, 'H', 'Pelusa', 5)

# print(pelusa.caminar())
# pelusa.comer()
# print(pelusa.Jugar())
# print(pelusa.Dormir())