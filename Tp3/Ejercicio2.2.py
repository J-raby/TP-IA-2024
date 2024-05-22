import math
import random
import time

MIN_X = -2
MAX_X = 2

#Para generar poblacion
def generate_poblacion(tam, restriccion_x, restriccion_y):
  poblacion = []
  for i in range(tam):
    individuo = {
      'x': random.uniform(restriccion_x[0], restriccion_x[1]),
      'y': random.uniform(restriccion_y[0], restriccion_y[1])
    }
    poblacion.append(individuo)
  
  return poblacion


#Para dar valor a individuo
# f(x, y) = 2 + sqrt(9 - x^2 - y^2)
def funcion_aptitud(ind):
  x = ind['x']
  y = ind['y']
  #Para que nos de valores positivos, x**2 e y**2 < 9
  res = math.sqrt(9 - (x**2) - (y**2))
  return (2 + res)

def tournament_selection(poblacion, tournament_size):
    winner_index = None
    tournament = random.sample(poblacion, tournament_size)
    aptitudes = [funcion_aptitud(individuo) for individuo in tournament]
    winner_index = aptitudes.index(max(aptitudes))
    return tournament[winner_index]

#Para ordenar 
def sort_by_fitness(poblacion):
  return sorted(poblacion, key=funcion_aptitud, reverse=True)

#Para cruzar
def cruzar(ind1, ind2):
  cruce_punto = random.randint(0,1)

  hijo = {
    'x': ind1['x'] if cruce_punto == 0 else ind2['x'],
    'y': ind1['y'] if cruce_punto == 0 else ind2['y']
  }

  return hijo

#Para mutar
def mutar(individuo):
  prox_x = individuo["x"] + random.uniform(-0.1, 0.1)
  prox_y = individuo["y"] + random.uniform(-0.1, 0.1)
  
  prox_x = min(max(prox_x, MIN_X), MAX_X)
  prox_y = min(max(prox_y, MIN_X), MAX_X)

  return {"x": prox_x, "y": prox_y}

#Para generar nueva gen
def generar_nueva_gen(prev_poblacion):
  prox_gen = []
  sorted_poblacion = sort_by_fitness(prev_poblacion)
  tam = len(prev_poblacion)
 
  for i in range(tam):
    #Seleccionamos dos individuos de entre los mas aptos
    padre = tournament_selection(sorted_poblacion, math.floor(tam * 0.5))
    madre = tournament_selection(sorted_poblacion, math.floor(tam * 0.5))
    #Los cruzamos y mutamos al resultante
    hijo = cruzar(madre, padre)
    hijo = mutar(hijo)

    prox_gen.append(hijo)
  
  return prox_gen


#Poblacion
pob = generate_poblacion(10, restriccion_x=(MIN_X,MAX_X), restriccion_y=(MIN_X,MAX_X))
i = 1
while True:
  print(f"🧬 GENERATION {i}")
  for ind in pob:
    print("Individuo: ", ind, "Fitness: ", funcion_aptitud(ind))
  #Que llegue hasta 0.1 el resultado
  if i == 100:
    break
  i+=1

  pob = generar_nueva_gen(pob)

best_individual = sort_by_fitness(pob)[0]
print("\n🔬 FINAL RESULT")
print(best_individual, funcion_aptitud(best_individual))