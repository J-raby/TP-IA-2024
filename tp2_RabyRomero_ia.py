import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

"""
Ejercicio 3

Columnas Categoricas: Tiempo
Columnas Numerica: Cantidad de goles por equipo local (HTHG)

Eliminar Columna: Referee

Eliminar Filas: HTHG (Como no tiene muchos valore nulos, imputamos por la mediana)

Imputar Filas: Tiros de local (HS), Tiempo

"""

file = pd.read_csv('./tp2/archive/past-data.csv')

# Contar los valores nulos y no nulos por columna
null_counts = file.isnull().sum()
non_null_counts = file.notna().sum()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(25, 10))

# Crear dos barras para cada columna, una para valores nulos y otra para no nulos
index = np.arange(len(file.columns))
bar_width = 0.35

rects1 = ax.bar(index - bar_width/2, null_counts, bar_width, label='Valores nulos')
rects2 = ax.bar(index + bar_width/2, non_null_counts, bar_width, label='Valores no nulos')

# Personalizar el gráfico
ax.set_xlabel('Columnas')
ax.set_ylabel('Cantidad de datos')
ax.set_xticks(index)
ax.set_xticklabels(file.columns)
ax.legend()

plt.tight_layout()
plt.show()


def graficarConNulos(columna):
    valores = columna.value_counts(dropna=False)
    indices = valores.index.astype(str)

    mapeo = dict(zip(indices, valores.values))
    sorted_mapeo_keys = sorted(mapeo.keys())
    sorted_mapeo = dict((key, mapeo[key]) for key in sorted_mapeo_keys)

    indices_sorted = list(sorted_mapeo.keys())
    valores_sorted = list(sorted_mapeo.values())


    # Alternatively, consider a single histogram with color-coding:
    plt.figure(figsize=(12, 6))  # Create a larger figure
    plt.bar(indices_sorted, valores_sorted)  # Use value as color
    plt.xlabel("Cantidad de Goles")
    plt.ylabel("Partidos")
    plt.title("Histogram de Goles de local en partidos")
    plt.show()
    

#Elejimos 2 columnas, FTHG y HS
# Selección de las columnas FTHG y HS
goles_local = file['HTHG']
tiros_local = file['HS']

graficarConNulos(goles_local)
graficarConNulos(tiros_local)



horas = file['Time']

valores_tiempo = horas.value_counts(dropna = False)
indices_tiempo = valores_tiempo.index.astype(str)


mapeo_hora = dict(zip(indices_tiempo, valores_tiempo.values))

sorted_mapeo_keys_hora = sorted(mapeo_hora.keys())
sorted_mapeo_tiempo = dict((key, mapeo_hora[key]) for key in sorted_mapeo_keys_hora)

nuevo_mapeo = {}

valores_tiempo_sorted = list(sorted_mapeo_tiempo.values())
indices_tiempo_sorted = list(sorted_mapeo_tiempo.keys())

plt.figure(figsize=(20, 14))  # Create a larger figure
plt.bar(indices_tiempo_sorted, valores_tiempo_sorted)  # Use value as color
plt.xlabel("Hora de partidos")
plt.ylabel("Cantidad de Partidos")
plt.title("Histogram de Goles de local en partidos")
plt.show()



# Eliminamos columna "Referee"
file = file.drop(columns='Referee')

# Eliminamos filas con nulos en "HTAG", "HTHG", "HTR"
file = file.dropna(axis=0,how='any',subset=['HTHG'])

# Imputamos las columnas HS y Tiempo
file['HS'].fillna(file['HS'].mean(), inplace=True)




# file['Time'] = file['Time'].astype(str)
# print(file['Time'].info())
# valores_a_tiempo = pd.to_datetime(file['Time'].dropna()).dt.strftime("%H:%M")


file['Time'].fillna(valores_a_tiempo.mode(), inplace=True)

