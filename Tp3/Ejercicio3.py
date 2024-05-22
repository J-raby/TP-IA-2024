from  sklearn.datasets import load_wine
from genetic_selection import GeneticSelectionCV # type: ignore
from sklearn.tree import DecisionTreeClassifier # type: ignore
import pandas as pd # type: ignore
import numpy as np

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
#Sacamos del dataset el valor que quieremos obtener
x = df.drop(['target'], axis=1)
#Lo pasamos como la columna y (resultado esperado)
y = df['target'].astype(float)

estimador = DecisionTreeClassifier()
modelo = GeneticSelectionCV(
    estimator=estimador, cv=4, verbose=1,
    scoring="accuracy", max_features=4,
    n_population=100, crossover_proba=0.5,
    mutation_proba=0.3, n_generations=50,
    crossover_independent_proba=0.5,
    mutation_independent_proba=0.04,
    tournament_size=3, n_gen_no_change=5,
    caching=True, n_jobs=-1
)
modelo = modelo.fit(x,y)
print('Features:', x.columns[modelo.support_])