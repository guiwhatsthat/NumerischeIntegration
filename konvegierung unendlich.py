import math
import matplotlib.pyplot as plt

# Implementierung der Methoden
def sekanten_trapez_regel(f, a, b, n):
    h = (b - a) / n
    x = a
    result = 0
    for i in range(1, n):
        result += h / 2 * (f(x) + f(x + h))
        x += h
    return result

def tangenten_trapez_regel(f, a, b, n):
    h = (b - a) / n
    x = a
    total = 0
    for i in range(n):
        midpoint = (x + x + h) / 2
        total += h * f(midpoint)
        x += h
    return total

def simpson_regel(f, a, b, n):
    h = (b - a) / n
    x = a
    total = 0
    for i in range(n):
        total += h / 6 * (f(x) + 4 * f((x + x + h) / 2) + f(x + h))
        x += h
    return total

# Definieren Sie die Funktion und die Grenzen
f = lambda x: math.pi * (1/x)
a, b = 1, 2

# Definieren Sie die Anzahl der Schritte für die Berechnung
steps = list(range(1, 101))

# Berechnen Sie die Approximationen für jeden Schritt
approx_sek = [sekanten_trapez_regel(f, a, b, n) for n in steps]
approx_tan = [tangenten_trapez_regel(f, a, b, n) for n in steps]
approx_sim = [simpson_regel(f, a, b, n) for n in steps]

# Plot der Ergebnisse
plt.figure(figsize=(10,6))
plt.plot(steps, approx_sek, label='Sekantentrapezregel')
plt.plot(steps, approx_tan, label='Tangententrapezregel')
plt.plot(steps, approx_sim, label='Simpson-Regel')
plt.legend()
plt.xlabel('Anzahl der Teilintervalle (n)')
plt.ylabel('Approximierte Integralwert')
plt.title('Vergleich der Integral-Approximationsmethoden')
plt.grid(True)
plt.show()