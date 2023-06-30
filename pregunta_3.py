'''¿Como afecta la edad de los jugadores en sus metricas de desempeño? Se observan
diferencias en las distintas posiciones: por ejemplo, para los arqueros?'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

data = pd.merge(df_1, df_2, how='outer')


correlation = data['age'].corr(data['overall'])

plt.figure(figsize=(12, 8))
plt.scatter(data['age'], data['overall'])
plt.xlabel('Edad')
plt.ylabel('Desempeño (Overall)')
plt.title(f'Correlación: {correlation:.2f}')
plt.show()
