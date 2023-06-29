import pandas as pd

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

data = pd.merge(df_1, df_2, how='outer')


def generalizar(elemento):
    for key, value in posiciones.items():
        if elemento in value:
            return key
    return elemento


posiciones = {'Goalkeeper': ['GK'], 'Defenders': ['CB', 'RB', 'LB'], 'Midfielders': [
    'CDM', 'CM', 'CAM', 'RM', 'LM'], 'Attackers': ['RW', 'LW', 'CF', 'ST']}

data = data[data['player_positions'].apply(generalizar).notna()]

print(data)

# data['player_positions'] = data['player_positions'].apply(generalizar)
