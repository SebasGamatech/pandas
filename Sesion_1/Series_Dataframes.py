#Vamos a importar la biblioteca Pandas y la llamamos pd
import pandas as pd
psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi', 'Cristiano'],
    #index=[1, 7, 10, 30, 40]
)
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi', 40: 'Cristiano'}
psg_players_dict = pd.Series(psg_dict)
#print(psg_players)
print(psg_players_dict)
print(psg_players_dict[7])
print(psg_players_dict[0:3])
#Diccionario con datos de jugadores
dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi', 'Cristiano'],
        'Altura': [183.0, 170.0, 170.0, 165.0, 187.0],
        'Goles': [2, 200, 150, 300, 100]}
#Crear un dataframe con el diccionario e índices personalizado
df = pd.DataFrame(dict, index=[1, 7, 10, 30, 40])
print(df)