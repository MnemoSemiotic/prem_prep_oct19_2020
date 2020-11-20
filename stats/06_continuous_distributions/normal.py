from math import e, pi, sqrt

def normal_pdf(x, mu, sigma):
    # hah, I was missing parens in the denominator!
    return (1 / (sigma * sqrt(2 * pi))) * e **(-(1/2) * ((x - mu)/sigma)**2)


def normal_cdf(x=0, mu=0, sigma=1):
    vals = [num*0.001 for num in range(-1000, int(x*1000))]

    area_accum = 0.0

    for val in vals:
        res = normal_pdf(val, mu, sigma)
        area_accum += res

        if val > x:
            break

    return area_accum*0.001


'''Example Slide 21'''
mu = 475
sigma = 98
x = 300

# print(normal_cdf(x, mu, sigma))


'''Breakout Slide 23'''
mu = 90
sigma = 10
x = 100

print(1 - normal_cdf(x, mu, sigma))
