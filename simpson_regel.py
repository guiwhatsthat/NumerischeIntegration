def simpson_regel(f, a, b, n):
    h = (b - a) / n  # Schrittweite
    x = a  # Startpunkt
    total = 0  # Gesamtsumme

    for i in range(n):
        # Simpson-Regel anwenden
        total += h / 6 * (f(x) + 4 * f((x + x + h) / 2) + f(x + h))
        x += h  # zum nächsten Teilintervall wechseln

    return total  # Approximation des Integrals