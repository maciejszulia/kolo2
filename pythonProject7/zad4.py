import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = {'a': np.random.randint(0,100,100),              #wektor a losowy przedział 0,100
        'b': np.random.randint(0,100,100),              #wektor b losowy przedział 0,100
        'c': np.random.randint(0,8,100)                 #wektor c losowy przedział 0,8
        }
data['d'] = np.abs(data['a'] - data['b'])               #wektor d tworzony z a - b

df = pd.DataFrame(data)                                 #zrob z tego dataframe

wykres = sns.relplot(data=df,x='a',y='b',palette='Set2', size='d')      #deklaracja wykres seaborna


plt.legend(loc='lower left')            #bla bla bla mat plot
plt.xlabel("os x")
plt.ylabel("os y")
plt.title("Wykres punktowy")
wykres.fig.set_size_inches(10, 10)
plt.show()
