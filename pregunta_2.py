'''¿Son los mejores jugadores tambien mejores pagados? Analice si esto es asi y si hay
otros factores que puedan impactar (el club, nacionalidad o puesto en el que juega)'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

data = pd.merge(df_1, df_2, how='outer')


def limpiar_nacionalidad(elemento):
    if elemento == 'Alemania':
        return 'Germany'
    if elemento == 'argentina':
        return 'Argentina'
    else:
        return elemento


def generalizar(elemento):
    for key, value in posiciones.items():
        if elemento in value:
            return key


data['nationality'] = data['nationality'].apply(limpiar_nacionalidad)

posiciones = {'Goalkeeper': ['GK'], 'Defenders': ['CB', 'RB', 'LB'], 'Midfielders': [
    'CDM', 'CM', 'CAM', 'RM', 'LM'], 'Attackers': ['RW', 'LW', 'CF', 'ST']}

data = data[data['player_positions'].apply(generalizar).notna()]

data['player_positions'] = data['player_positions'].apply(generalizar)

# Grafico 1
x_var = 'player_positions'
y_var = 'wage_eur'
x = data[x_var]
y = data[y_var]

fig, ax = plt.subplots(figsize=(10, 6))

promedio = data.groupby(x_var)[y_var].mean().reset_index()

plt.bar(promedio[x_var], promedio[y_var],
        color='blue', label='Promedio sueldo por posicion', alpha=0.4)

for i in range(len(promedio)):
    plt.text(i, promedio[y_var][i], f'${promedio[y_var][i]:.2f}')

plt.xlabel('Posicion')
plt.ylabel('Salario en euros')
plt.title('Salario en euros por posicion')
plt.xticks(rotation=90)
plt.legend()
plt.show()
