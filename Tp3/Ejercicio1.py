import random
import time

class Entidad:
    OBJETIVO = "Los algoritmos genéticos sirven para optimizar"
    GENES = '''aábcdeéfghiíjklmnoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNOÓP
    QRSTUÚVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

    def __init__(self, prop):
        self.prop = prop
        self.fitness = self.get_fitness()
    
    @classmethod
    def generar_gen(cls):
        return ''.join(random.choices(cls.GENES, k=len(cls.OBJETIVO)))
    
    def cruzar(self, pareja):
        punto1 = random.randint(1, len(self.prop) - 2)
        punto2 = random.randint(punto1 + 1, len(self.prop) - 1)
        gen1 = self.prop[:punto1] + pareja.prop[punto1:punto2] + self.prop[punto2:]
        gen2 = pareja.prop[:punto1] + self.prop[punto1:punto2] + pareja.prop[punto2:]
        return [Entidad(gen1), Entidad(gen2)]
    
    def mutar(self, tasa_mutacion=0.01):
        prop_mutada = list(self.prop)
        for i in range(len(prop_mutada)):
            if random.random() < tasa_mutacion:
                prop_mutada[i] = random.choice(self.GENES)
        self.prop = ''.join(prop_mutada)
        self.fitness = self.get_fitness()
    
    def get_fitness(self):
        return sum(1 for c1, c2 in zip(self.prop, self.OBJETIVO) if c1 != c2)

def generate_poblacion(size):
    return [Entidad(Entidad.generar_gen()) for _ in range(size)]

def rueda_ruleta(poblacion):
    total_fitness = sum(1 / (ind.fitness + 1) for ind in poblacion)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in poblacion:
        current += 1 / (ind.fitness + 1)
        if current > pick:
            return ind

def main():
    tamanios_poblaciones = [100,1000,50,200,300,500]
    resultados = {}
    for tam in tamanios_poblaciones:
        start_time = time.time()
        poblacion = generate_poblacion(tam)
        poblacion.sort(key=lambda x: x.fitness)
    
        generacion = 0
        while poblacion[0].fitness != 0:
            nueva_generacion = poblacion[:10]  # Mantener a los mejores 10 individuos (élite)
            while len(nueva_generacion) < len(poblacion):
                padre = rueda_ruleta(poblacion)
                madre = rueda_ruleta(poblacion)
                hijos = padre.cruzar(madre)
                for hijo in hijos:
                    hijo.mutar(tasa_mutacion=0.01)
                    nueva_generacion.append(hijo)
        
            nueva_generacion.sort(key=lambda x: x.fitness)
            poblacion = nueva_generacion[:len(poblacion)]
        
            #print(f"Generacion {generacion} - mejor fitness: {poblacion[0].fitness} - gen: {poblacion[0].prop}")
            generacion += 1
        stop_time = time.time()
        resultados[tam] = {
            'generations' : generacion,
            'tiempo' : stop_time - start_time
        }
        print(f"Solución encontrada en la generación {generacion}: {poblacion[0].prop} --- en un tiempo de {stop_time - start_time} usando un tamaño de poblacion de {tam}" )

    print(resultados)

    #En base a los distintos tamaños, notamos que entre mas grande es la poblacion mas se tarda en pasar de generacion en generacion, mientras que en poblaciones mas pequeñas
    # se usan mas generaciones para llegar al resultado pero el paso es más rápido. Por lo que lo mejor es usar poblaciones pequeñas cuando lo importante es el tiempo y poblaciones
    # grandes cuando lo importante es la menor cantidad de generaciones.

if __name__ == "__main__":
    main()
