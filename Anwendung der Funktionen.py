import math

# Funktionen
def sekanten_trapez_regel(f, a, b, n):
    # Berechnung der Breite jedes Teilintervalls
    h = (b - a) /n 
    
    #Initalisierung x
    x = a

    # Initialisierung des Resultats (Summe)
    result = 0

    # Berechnung der Summe
    for i in range(1, n):
        result += h/2 * (f(x)+ f(x + h))
        x += h

    return result

def tangenten_trapez_regel(f, a, b, n):
    h = (b - a) / n  # Schrittweite
    x = a  # Startpunkt
    total = 0  # Gesamtsumme

    for i in range(n):
        # Tangententrapezregel anwenden
        midpoint = (x + x + h) / 2  # Mittelpunkt des aktuellen Teilintervalls
        total += h * f(midpoint)  # Funktionswert an der Mittelpunktstelle mit Schrittweite multiplizieren
        x += h  # zum nächsten Teilintervall wechseln

    return total  # Approximation des Integrals

def simpson_regel(f, a, b, n):
    h = (b - a) / n  # Schrittweite
    x = a  # Startpunkt
    total = 0  # Gesamtsumme

    for i in range(n):
        # Simpson-Regel anwenden
        total += h / 6 * (f(x) + 4 * f((x + x + h) / 2) + f(x + h))
        x += h  # zum nächsten Teilintervall wechseln

    return total  # Approximation des Integrals


# Definieren Sie die Funktionen für die Integrale
f1 = lambda x: math.pi * (1/x)
f2 = lambda x: x**3 + 3*x**2
f3 = lambda x: math.cos(x)

# Definieren Sie die Grenzen und die Anzahl der Streifen
a1, b1, n1 = 1, 2, 100
a2, b2, n2 = 0, 1, 100
a3, b3, n3 = -math.pi/2, math.pi/2, 100

# Berechnen Sie die Approximationen
approx1_sek = sekanten_trapez_regel(f1, a1, b1, n1)
approx1_tan = tangenten_trapez_regel(f1, a1, b1, n1)
approx1_sim = simpson_regel(f1, a1, b1, n1)

approx2_sek = sekanten_trapez_regel(f2, a2, b2, n2)
approx2_tan = tangenten_trapez_regel(f2, a2, b2, n2)
approx2_sim = simpson_regel(f2, a2, b2, n2)

approx3_sek = sekanten_trapez_regel(f3, a3, b3, n3)
approx3_tan = tangenten_trapez_regel(f3, a3, b3, n3)
approx3_sim = simpson_regel(f3, a3, b3, n3)

# Drucken Sie die Ergebnisse
print("Approximationen für das erste Integral:")
print("Sekantentrapezregel: ", approx1_sek)
print("Tangententrapezregel: ", approx1_tan)
print("Simpsonsche Regel: ", approx1_sim)

print("\nApproximationen für das zweite Integral:")
print("Sekantentrapezregel: ", approx2_sek)
print("Tangententrapezregel: ", approx2_tan)
print("Simpsonsche Regel: ", approx2_sim)

print("\nApproximationen für das dritte Integral:")
print("Sekantentrapezregel: ", approx3_sek)
print("Tangententrapezregel: ", approx3_tan)
print("Simpsonsche Regel: ", approx3_sim)

import sympy as sp

# Definieren Sie die Symbole
x = sp.symbols('x')

# Definieren Sie die Funktionen für die Integrale
f1_sympy = sp.pi * (1/x)
f2_sympy = x**3 + 3*x**2
f3_sympy = sp.cos(x)

# Berechnen Sie die exakten Werte der Integrale
exact1 = sp.integrate(f1_sympy, (x, a1, b1))
exact2 = sp.integrate(f2_sympy, (x, a2, b2))
exact3 = sp.integrate(f3_sympy, (x, a3, b3))

# Drucken Sie die exakten Werte und die Differenzen zu den Approximationen
print("Exakter Wert und Differenz für das erste Integral:")
print("Exakter Wert: ", exact1)
print("Differenz Sekantentrapezregel: ", exact1 - approx1_sek)
print("Differenz Tangententrapezregel: ", exact1 - approx1_tan)
print("Differenz Simpsonsche Regel: ", exact1 - approx1_sim)

print("\nExakter Wert und Differenz für das zweite Integral:")
print("Exakter Wert: ", exact2)
print("Differenz Sekantentrapezregel: ", exact2 - approx2_sek)
print("Differenz Tangententrapezregel: ", exact2 - approx2_tan)
print("Differenz Simpsonsche Regel: ", exact2 - approx2_sim)

print("\nExakter Wert und Differenz für das dritte Integral:")
print("Exakter Wert: ", exact3)
print("Differenz Sekantentrapezregel: ", exact3 - approx3_sek)
print("Differenz Tangententrapezregel: ", exact3 - approx3_tan)
print("Differenz Simpsonsche Regel: ", exact3 - approx3_sim)


import numpy as np
import matplotlib.pyplot as plt
# Erstellen Sie Listen mit den exakten Werten und den Approximationen
exact_values = [exact1, exact2, exact3]
sek_values = [approx1_sek, approx2_sek, approx3_sek]
tan_values = [approx1_tan, approx2_tan, approx3_tan]
sim_values = [approx1_sim, approx2_sim, approx3_sim]

# Erstellen Sie die Balkendiagramme
labels = ['Exakter Wert', 'Sekantentrapezregel', 'Tangententrapezregel', 'Simpsonsche Regel']
x = np.arange(len(labels))
width = 0.35

# Integral von pi * (1/x)
fig1, ax1 = plt.subplots()
rects1 = ax1.bar(x, [exact_values[0], sek_values[0], tan_values[0], sim_values[0]], width)
ax1.set_ylabel('Wert des Integrals')
ax1.set_title('Vergleich der exakten Werte und der Approximationen für das Integral von pi * (1/x)')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)

# Setze die Begrenzungen der y-Achse
ax1.set_ylim([2, 2.4])

# Zeichne eine Linie für den exakten Wert
ax1.axhline(y=exact_values[0], color='r', linestyle='--')

# Integral von x^3 + 3*x^2
fig2, ax2 = plt.subplots()
rects2 = ax2.bar(x, [exact_values[1], sek_values[1], tan_values[1], sim_values[1]], width)
ax2.set_ylabel('Wert des Integrals')
ax2.set_title('Vergleich der exakten Werte und der Approximationen für das Integral von x^3 + 3*x^2')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)

# Setze die Begrenzungen der y-Achse
ax2.set_ylim([1, 1.4])

# Zeichne eine Linie für den exakten Wert
ax2.axhline(y=exact_values[1], color='r', linestyle='--')

# Integral von cos(x)
fig3, ax3 = plt.subplots()
rects3 = ax3.bar(x, [exact_values[2], sek_values[2], tan_values[2], sim_values[2]], width)
ax3.set_ylabel('Wert des Integrals')
ax3.set_title('Vergleich der exakten Werte und der Approximationen für das Integral von cos(x)')
ax3.set_xticks(x)
ax3.set_xticklabels(labels)

# Setze die Begrenzungen der y-Achse
ax3.set_ylim([1.75, 2.2])

# Zeichne eine Linie für den exakten Wert
ax3.axhline(y=exact_values[2], color='r', linestyle='--')

plt.show()