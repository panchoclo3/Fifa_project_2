'''¿Son los mejores jugadores tambien mejores pagados? Analice si esto es asi y si hay
otros factores que puedan impactar (el club, nacionalidad o puesto en el que juega)'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

data = pd.merge(df_1, df_2, how='outer')

posiciones = {'GK': 'Goal keeper', 'CB': 'Center back', 'RB': 'Right back', 'LB': 'Left back', 'CDM': 'Center defensive midfielder', 'CM': 'Center midfielder',
              'CAM': 'Center attacking midfielder', 'RM': 'Right midfielder', 'LM': 'Left midfielder', 'RW': 'Right winger', 'LW': 'Left winger', 'CF': 'Center forward', 'ST': 'Striker'}

# plt.scatter(data['league_rank'], data['wage_eur'])
# plt.xlabel('Rango de liga')
# plt.ylabel('Sueldo en euros')
# plt.title('Sueldo de jugadores segun rango de liga')
# plt.xticks(rotation=90)
# plt.show()
