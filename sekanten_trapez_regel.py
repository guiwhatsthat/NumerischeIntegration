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