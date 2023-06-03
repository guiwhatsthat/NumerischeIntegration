from sympy import symbols
from sympy.integrals.quadrature import gauss_legendre

x = symbols('x')
n = 5  # Ordnung der Quadratur

# Gauss-Legendre-Punkte und -Gewichte für Ordnung n
xi, wi = gauss_legendre(n, 15)

# Berechnung des Integrals
integral_approximation = sum(w * f.subs(x, x_val) for x_val, w in zip(xi, wi))