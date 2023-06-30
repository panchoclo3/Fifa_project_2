'''¿Son los mejores jugadores tambien mejores pagados? Analice si esto es asi y si hay
otros factores que puedan impactar (el club, nacionalidad o puesto en el que juega)'''

from scipy.stats import f_oneway
from statsmodels.formula.api import ols
import statsmodels.api as sm
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


# Carga los datos en un DataFrame

data['club_code'] = pd.factorize(data['club_name'])[0]

model = ols('wage_eur ~ C(club_code)', data=data).fit()
anova_table = sm.stats.anova_lm(model)

print(anova_table)


result = f_oneway(*[group['wage_eur']
                  for name, group in data.groupby('club_name')])

print("Estadística F:", result.statistic)
print("Valor p:", result.pvalue)
