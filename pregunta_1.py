'''Una creencia popular es que los jugadores de Brasil son los mejores jugadores de
latinoamerica. Es esto real? Son los mejores en cuanto al score general? y a otras
metricas mas especificas (analice con al menos 2 metricas, distintas al score)?'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

df = pd.merge(df_1, df_2, how='outer')


def filtro(elemento):
    paises = ['Brazil', 'Argentina', 'Uruguay', 'Chile',
              'Colombia', 'Peru', 'Paraguay', 'Ecuador', 'Venezuela', 'Bolivia']
    return elemento in paises


df = df[df['nationality'].apply(filtro)]

df.dropna(inplace=True)


def graficar(columna, titulo):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['nationality'], df[columna], alpha=0.5)
    promedio = df.groupby('nationality')[columna].mean().reset_index()
    plt.bar(promedio['nationality'],
            promedio[columna], color='blue', label=f'Promedio {titulo}', alpha=0.4)
    plt.xlabel('Nacionalidad')
    plt.ylabel(titulo)
    plt.title(f'{titulo} de los jugadores por nacionalidad')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()


# graficar('overall', 'Score general')
# graficar('value_eur', 'Valor en euros')
# graficar('wage_eur', 'Salario en euros')
graficar('league_rank', 'Ranking de la liga')
