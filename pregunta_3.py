'''¿Como afecta la edad de los jugadores en sus metricas de desempeño? Se observan
diferencias en las distintas posiciones: por ejemplo, para los arqueros?'''

import pandas as pd
import matplotlib.pyplot as plt

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

data = pd.merge(df_1, df_2, how='outer')


def graficar_por_posicion(titulo, posicion):
    df = data[data['player_positions'].str.contains(posicion)]
    correlation = df['age'].corr(df['overall'])

    if correlation > 0.5:
        plt.figure(figsize=(12, 8))
        plt.scatter(df['age'], df['overall'])
        plt.xlabel('Edad')
        plt.ylabel('Desempeño (Overall)')
        plt.title(f'{titulo}\nCorrelacion: {correlation:.2f}')
        plt.show()


posiciones = {'GK': 'Goal keeper', 'CB': 'Center back', 'RB': 'Right back', 'LB': 'Left back', 'CDM': 'Center defensive midfielder', 'CM': 'Center midfielder',
              'CAM': 'Center attacking midfielder', 'RM': 'Right midfielder', 'LM': 'Left midfielder', 'RW': 'Right winger', 'LW': 'Left winger', 'CF': 'Center forward', 'ST': 'Striker'}

for elemento in posiciones.items():
    graficar_por_posicion(elemento[1], elemento[0])
