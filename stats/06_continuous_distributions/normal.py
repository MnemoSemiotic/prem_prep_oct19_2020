from math import e, pi, sqrt

def normal_pdf(x, mu, sigma):
    return (1 / sigma * sqrt(2 * pi)) * e **(-(1/2) * ((x - mu)/sigma)**2)