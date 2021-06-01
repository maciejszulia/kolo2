import pandas as pd
import matplotlib.pyplot as plt

# Załaduj ramkę danych na podstawie pliku cars.csv
df = pd.read_csv('cars.csv', header=0, sep=';', decimal='.')
print(df)

# Stwórz nową ramkę danych składającą się z wierszy, dla których w kolumnie „Weight” wartość jest mniejsza niż 2200.
df_zad2 = df[df['Weight'] > 2200]
print(df_zad2)

# Na nowej ramce danych utwórz grupę po kolumnie „Model year”,
# a następnie policz średnią moc silnika (kolumna „Horsepower”)
# dla poszczególnego rocznika samochodu

df_zad3 = df.groupby(['Model year'])        # grupa po kolumnie
df_zad3 = df_zad3.mean()                    # średnią moc silnika
df_zad3 = df_zad3['Horsepower']             # pokaz tylko model year i horsepower
print(df_zad3)

# Przedstaw wynik z poprzedniego podpunktu na wykresie słupkowym,
# dodaj tytuł do wykresu oraz etykiety osi x oraz y.

wykres = df_zad3.plot.bar()     #pie - koło
plt.title("avg horsepower by year") # tytuł
plt.ylabel("moc")
plt.xlabel("rocznik")

# Wykres zapisz w formacie png.
plt.savefig("wykres.png")
plt.show()
