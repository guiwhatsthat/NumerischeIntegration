import numpy as np
import matplotlib.pyplot as plt

# Definieren Sie den Bereich für x
x = np.linspace(-10, 10, 1000)

# Berechnen Sie y
y = np.sin(x)

# Erstellen Sie die Figur und die Achsen
fig, ax = plt.subplots()

# Zeichnen Sie die Sinusfunktion
ax.plot(x, y, 'b', linewidth=2)

# Zeichnen Sie eine durchgehende schwarze Linie bei y=0
ax.axhline(0, color='black')

# Fügen Sie "Spikes" bei den auf der x-Achse angegebenen Werten hinzu
ax.set_xticks(np.arange(-10, 11, 1))
ax.grid(True, which='both', axis='x', linestyle='--')

# Setzen Sie die Grenzen und die Beschriftungen der Achsen
ax.set_xlim([-10, 10])
ax.set_ylim([-1.5, 1.5])
ax.set_xlabel('x')
ax.set_ylabel('y=sin(x)')

# Zeigen Sie das Diagramm
plt.show()
