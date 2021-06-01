# Za pomocą biblioteki matplotlib odwzoruj wykres dostępny w pliku zad2a.png

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100, 0.1)                       # generuje liste [-100,100  step 0.1]
plt.subplot(1, 3, 1)                                # pozycja wykresa
plt.plot(x, x ** 2 - 4 * x + 2, label="x^2-4x+2")   # funkcja x
plt.axis([0, 10, -10, 50])                          # zakres [x od, x do, y od, y do]
plt.legend(loc="lower left")                        # legenda
plt.title("pierwszy wykres")                        # tytul
plt.grid()                                          # daj siatke



plt.subplot(1, 3, 2)  # pozycja wykresa
plt.plot(x, pow(x, 3)-pow(2,x)-4*x, "go", label="x^3-2^x-4x")
plt.axis([0, 10, -99, 249])
plt.legend(loc="lower center")
plt.title("drugi wykres")
plt.grid()



plt.subplot(1, 3, 3)  # pozycja wykresa
plt.plot(x, x ** 2 - 4 * x + 2, label="x^2-4x+2")
plt.plot(x, pow(x, 3)-pow(2,x)-4*x, "go", label="x^3-2^x-4x")
plt.axis([0, 10, -10, 50])
plt.legend(loc="upper center")
plt.title("trzeci wykres")
plt.grid()

plt.show()