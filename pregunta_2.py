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

data['preferred_foot'] = data['preferred_foot'].str.lower()

data['nationality'] = data['nationality'].apply(limpiar_nacionalidad)

posiciones = {'Goalkeeper': ['GK'], 'Defenders': ['CB', 'RB', 'LB'], 'Midfielders': [
    'CDM', 'CM', 'CAM', 'RM', 'LM'], 'Attackers': ['RW', 'LW', 'CF', 'ST']}

data = data[data['player_positions'].apply(generalizar).notna()]

data['player_positions'] = data['player_positions'].apply(generalizar)

# Grafico 1
# x_var = 'player_positions'
# y_var = 'wage_eur'
# x = data[x_var]
# y = data[y_var]
# 
# fig, ax = plt.subplots(figsize=(10, 6))
# 
# promedio = data.groupby(x_var)[y_var].mean().reset_index()
# 
# plt.bar(promedio[x_var], promedio[y_var],
#         color='blue', label='Promedio sueldo por posicion', alpha=0.4)
# 
# for i in range(len(promedio)):
#     plt.text(i, promedio[y_var][i], f'${promedio[y_var][i]:.2f}')
# 
# plt.xlabel('Posicion')
# plt.ylabel('Salario en euros')
# plt.title('Salario en euros por posicion')
# plt.xticks(rotation=90)
# plt.legend()
# plt.show()

# Grafico 2
nationality = {'Europe': ['Germany', 'Spain', 'England', 'France', 'Italy', 'Netherlands', 'Portugal', 'Russia', 'Belgium', 'Denmark', 'Sweden', 'Switzerland', 'Poland', 'Turkey', 'Ukraine', 'Austria', 'Croatia', 'Greece', 'Czech Republic', 'Serbia', 'Norway', 'Scotland', 'Ireland', 'Romania', 'Hungary', 'Slovakia', 'Bosnia Herzegovina', 'Albania', 'Slovenia', 'Bulgaria', 'Finland', 'Montenegro', 'North Macedonia', 'Iceland', 'Wales', 'Estonia', 'Armenia', 'Georgia', 'Cyprus', 'Luxembourg', 'Azerbaijan', 'Kosovo', 'Faroe Islands', 'Malta', 'Liechtenstein', 'Gibraltar', 'San Marino', 'Andorra', 'Latvia', 'Lithuania', 'Moldova'],
               'Asia':['China', 'Japan', 'Saudi Arabia', 'South Korea', 'United Arab Emirates', 'Uzbekistan', 'Vietnam'], 
              'South America': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Paraguay', 'Peru', 'Uruguay'], 
              'North America': ['Canada', 'Costa Rica', 'Mexico', 'United States'],
              'Center America': ['Honduras', 'Jamaica', 'Panama'],
              'Africa': ['Algeria', 'Angola', 'Benin', 'Burkina Faso', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Comoros', 'Congo', 'DR Congo', 'Egypt', 'Equatorial Guinea', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea Bissau', 'Ivory Coast', 'Kenya', 'Liberia', 'Libya', 'Madagascar', 'Mali', 'Morocco', 'Mozambique', 'Nigeria', 'Senegal', 'Sierra Leone', 'South Africa', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'], 
              'Oceania': ['Australia', 'New Zealand'],}

def generalizar_nacionalidad(elemento):
    for key, value in nationality.items():
        if elemento in value:
            return key

data['continent'] = data['nationality'].apply(generalizar_nacionalidad)

data['nationality'] = data['nationality'].apply(generalizar_nacionalidad)

print(data['continent'])
 
# plt.figure(figsize=(10, 6))
# plt.scatter(data['nationality'], data['wage_eur'], alpha=0.4)
# plt.xlabel('Nacionalidad')
# plt.ylabel('Salario en euros')
# plt.title('Salario en euros por nacionalidad')
# plt.xticks(rotation=90)
# plt.show()

# correlacion entre foto preferido y score general
plt.figure(figsize=(10, 6))
plt.scatter(data['preferred_foot'], data['overall'], alpha=0.4)
plt.xlabel('Score general')
plt.ylabel('Pie preferido')
plt.title('Correlacion entre pie preferido y score general')
plt.show()

# tes de hipotesis entre pie preferido y score general
from scipy.stats import ttest_ind


# H0: no hay diferencia entre los pies preferidos y el score general
# H1: si hay diferencia entre los pies preferidos y el score general
resultado = ttest_ind(data[data['preferred_foot'] == 'left']['overall'], data[data['preferred_foot'] == 'right']['overall'])
print(resultado)