#Funcion
#z - x**2 - 15y**2 -2 < x,y,z < 11

import math
import random
import time

MIN_X = -2
MAX_X = 11

#Para generar poblacion
def generate_poblacion(tam, restriccion_x, restriccion_y, restriccion_z):
  poblacion = []
  for i in range(tam):
    individuo = {
      'x': random.uniform(restriccion_x[0], restriccion_x[1]),
      'y': random.uniform(restriccion_y[0], restriccion_y[1]),
      'z': random.uniform(restriccion_z[0], restriccion_z[1])
    }
    poblacion.append(individuo)
  
  return poblacion


#Para dar valor a individuo
#z - x**2 - 15y**2 
def funcion_aptitud(ind):
  x = ind['x']
  y = ind['y']
  z = ind['z']
  return z - x**2 - 15*y**2

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
  cruce_punto = random.randint(0,2)

  hijo = {
    'x': ind1['x'] if cruce_punto == 0 else ind2['x'],
    'y': ind1['y'] if cruce_punto == 1 else ind2['y'],
    'z': ind1['z'] if cruce_punto == 2 else ind2['z']
  }

  return hijo

#Para mutar
def mutar(individuo):
  prox_x = individuo["x"] + random.uniform(-0.1, 0.1)
  prox_y = individuo["y"] + random.uniform(-0.1, 0.1)
  prox_z = individuo["z"] + random.uniform(-0.1, 0.1)
  
  prox_x = min(max(prox_x, MIN_X), MAX_X)
  prox_y = min(max(prox_y, MIN_X), MAX_X)
  prox_z = min(max(prox_z, MIN_X), MAX_X)

  return {"x": prox_x, "y": prox_y, "z": prox_z}

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
pob = generate_poblacion(100, restriccion_x=(MIN_X,MAX_X), restriccion_y=(MIN_X,MAX_X),restriccion_z=(MIN_X,MAX_X))
i = 1
while True:
  print(f"🧬 GENERATION {i}")
  for ind in pob:
    print("Individuo: ", ind, "Fitness: ", funcion_aptitud(ind))
  #Que llegue hasta 0.1 el resultado
  if i == 50:
    break
  i+=1

  pob = generar_nueva_gen(pob)

best_individual = sort_by_fitness(pob)[0]
print("\n🔬 FINAL RESULT")
print(best_individual, funcion_aptitud(best_individual))