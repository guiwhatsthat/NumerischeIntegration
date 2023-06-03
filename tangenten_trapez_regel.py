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
