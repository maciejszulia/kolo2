# Wykorzystując plik z zadania pierwszego utwórz wykres kołowy obrazujący informację
# dotyczącą ilości cylindrów(kolumna „Cylinders”)w samochodach marki ford.
# Procentowe wartości mają być zaokrąglone do dwóch miejsc po przecinku,
# rozmiar czcionki na wykresie to 14, wyświetl legendę oraz tytuł wykresu.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv', header=0, sep=';', decimal='.') #wczytaj csv

df = df[['Cylinders', 'Car name']]                   #wyciągnij 2kolumny
df.sort_values("Car name")                           #posortuj po car name
df2 = df[(df['Car name'].str[:4] == 'ford')]       #sprawdzanko czy pierwsze 4 litery to ford
df3 = df2.groupby(['Cylinders']).agg({'Cylinders': ['count']})  #w df2 są tylko fordy
                                                                #grupuje sie wedle cylindrów
                                                                #+ liczy ile jest cylindrów

print(df3)

wykres = df3.plot.pie(subplots=True, autopct='%.2f %%')
plt.title('aaaa')
plt.legend(loc=False)
plt.show()
