import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df_1 = pd.read_csv('fifa2021_1.csv')
df_2 = pd.read_csv('fifa2021_2.csv')

data = pd.merge(df_1, df_2, how='outer')


x_values = np.linspace(start=150, stop=220, num=1000)

x_var = "height_cm"
y_var = "weight_kg"

x = data[x_var]
y = data[y_var]

slope, intercept = np.polyfit(x, y, 1)
regression_line = slope * x_values + intercept
plt.style.use('seaborn')
plt.scatter(x, y, color='green', alpha=0.3)
plt.scatter(x_values, regression_line, c='red', s=0.8)
plt.xlabel(x_var)
plt.ylabel(y_var)

plt.title('Relacion entre altura y peso de los jugadores')
plt.show()

continents = {
    'Africa': ['Senegal', 'Egypt', 'Cameroon', 'Ghana', 'Morocco', 'Burkina Faso', 'Mali', 'Angola', 'Cape Verde', 'Zambia', 'Gambia', 'Kenya', 'Gabon', 'Libya', 'South Africa', 'Sierra Leone', 'Madagascar', 'Tunisia', 'Equatorial Guinea', 'Uganda', 'Guinea Bissau'],
    'Asia': ['Japan', 'United Arab Emirates', 'Armenia', 'Azerbaijan', 'Saudi Arabia', 'South Korea', 'China', 'Uzbekistan', 'Vietnam'],
    'Europe': ['Slovenia', 'Poland', 'Germany', 'Netherlands', 'Belgium', 'Spain', 'England', 'France', 'Scotland', 'Italy', 'Croatia', 'Switzerland', 'Slovakia', 'Portugal', 'Hungary', 'Norway', 'Albania', 'Sweden', 'Wales', 'Bosnia Herzegovina', 'Finland', 'Serbia', 'Montenegro', 'Ukraine', 'Turkey', 'Kosovo', 'Georgia', 'Iceland', 'Jamaica', 'Moldova', 'Luxembourg', 'Bulgaria', 'Latvia', 'Liechtenstein', 'Faroe Islands', 'Andorra', 'Cyprus'],
    'North America': ['Mexico', 'Canada', 'United States'],
    'South America': ['Argentina', 'Uruguay', 'Colombia', 'Ecuador', 'Peru', 'Paraguay', 'Chile', 'Brazil'],
    'Oceania': ['Australia', 'New Zealand'],
    'Central America': ['Costa Rica', 'Panama', 'Honduras', 'Jamaica'],
}
