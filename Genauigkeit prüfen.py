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