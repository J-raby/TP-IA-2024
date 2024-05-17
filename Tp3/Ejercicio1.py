import random
import string

class Entidad(object):
    
    def __init__(self, prop):
        self.prop = prop
        self.fitness = self.get_fitness()
    
    @classmethod
    def generar_gen(self):
        global GENES
        global OBJETIVO
        res = ''.join(random.choices(OBJETIVO, k=len(OBJETIVO)))
        return res
    

    def get_fitness(self):
        global OBJETIVO
        current = 0
        for c1, c2 in zip(self.prop, OBJETIVO):
            if c1 != c2:
                current+=1
        return current
    
#PROCESO DE AG

#1 - POBLACION
#Posibles genes
GENES = '''aábcdeéfghiíjklmnoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNOÓP
QRSTUÚVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

#Resultado esperado
OBJETIVO = "Los algoritmos genéticos sirven para optimizar"

def generate_poblacion(size):
    poblacion = []
    for i in range(0, size):
        gen = Entidad.generar_gen()
        ind = Entidad(gen)
        poblacion.append(ind)
    return poblacion

poblacion = generate_poblacion(100)
poblacion.sort(key= lambda x:x.fitness)

for ind in poblacion:
    print(ind.prop)
#2 - FUNCIÓN DE APTITUD
#Generamos la poblacion y al mismo se le da a cada entidad un valor de aptitud
#La funcion que se usa en este caso es diferencia entre caracteres

def rueda_ruleta(poblacion):
    total_fitness = sum(ind.fitness for ind in poblacion)

    pick = random.uniform(0, total_fitness)

    i = 0
    for ind in poblacion:
        i += ind.fitness
        if i > pick:
            return ind

seleccionar = rueda_ruleta(poblacion)

print(f"{seleccionar.prop}, : {seleccionar.fitness}")

#3 - SELECCION
#Usamos metodo de la ruleta para seleccionar los mejores genes


