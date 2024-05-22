from math import sqrt
import random

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
#  f(x, y) = (x − 1)^2 + (x − y)^ 4
def funcion_aptitud(ind):
  x = ind['x']
  y = ind['y']
  return (x - 1)**2 + (x - y)**4


# Para seleccionar
def metodo_ruleta(ord_poblacion, tot_fitness):
    offset = 0
    tf = tot_fitness

    min_fitness = funcion_aptitud(ord_poblacion[0])
    if min_fitness < 0:
        offset = -min_fitness
        tf += offset * len(ord_poblacion)

    draw = random.uniform(0, 1)

    acumulado = 0
    for ind in ord_poblacion:
        fitness = funcion_aptitud(ind) + offset
        acumulado += fitness

        if draw <= acumulado:
            return ind


#Para ordenar 
def sort_by_fitness(poblacion):
  return sorted(poblacion, key=funcion_aptitud)

#Para cruzar
def cruzar(ind1, ind2):
  xa = ind1["x"]
  ya = ind1["y"]

  xb = ind2["x"]
  yb = ind2["y"]

  return {"x":  (xa + xb) / 2, "y": (ya + yb) / 2}

#Para mutar
def mutar(individuo):
  prox_x = individuo["x"] + random.uniform(-0.05, 0.05)
  prox_y = individuo["y"] + random.uniform(-0.05, 0.05)
  
  prox_x = min(max(prox_x, -5), 5)
  prox_y = min(max(prox_y, -5), 5)

  return {"x": prox_x, "y": prox_y}

#Para generar nueva gen
def generar_nueva_gen(prev_poblacion):
  prox_gen = []
  sorted_poblacion = sort_by_fitness(prev_poblacion)
  tam = len(prev_poblacion)
  tf = sum(funcion_aptitud(ind) for ind in prev_poblacion)

  for i in range(tam):
    #Seleccionamos dos individuos de entre los mas aptos
    madre = metodo_ruleta(sorted_poblacion, tf)
    padre = metodo_ruleta(sorted_poblacion, tf)
    #Los cruzamos y mutamos al resultante
    hijo = cruzar(madre, padre)
    hijo = mutar(hijo)

    prox_gen.append(hijo)
  
  return prox_gen


#Poblacion
pob = generate_poblacion(100, restriccion_x=(-5,5), restriccion_y=(-5,5))
i = 1
while True:
  print(f"🧬 GENERATION {i}")
  for ind in pob:
    print("Individuo: ", ind, "Fitness: ", funcion_aptitud(ind))
  #Que llegue hasta 0.1 el resultado
  if i == 500 or funcion_aptitud(ind) < 0.1:
    break
  i+=1

  pob = generar_nueva_gen(pob)

best_individual = sort_by_fitness(pob)[0]
print("\n🔬 FINAL RESULT")
print(best_individual, funcion_aptitud(best_individual))




#Funcion de aptitud

## -- La funcion de aptitud seria reemplazar los valores en la funcion principal
## -- por los valores de los individuos de la poblacion

#Seleccion

#Cruzamiento

#Mutacion

def main(args):
   
   


if __name__ == '__main__':
   main()