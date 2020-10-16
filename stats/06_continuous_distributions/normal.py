from math import e, pi, sqrt

def normal_pdf(x, mu, sigma):
    return (1 / sqrt(2*pi*sigma**2) * e**((-(1/2)*((x-mu)**2 / sigma**2))))


def normal_cdf(x=0, mu=0, sigma=2):
    vals = [num*0.001 for num in range(-10000, int(x*1000))]

    # vals = []
    
    # for num in range(-10000, int(x*1000)):
    #     vals.append(num*0.001)

    area_accum = 0.0

    for val in vals:
        res = normal_pdf(val, mu, sigma)
        area_accum += res

        if val > x:
            break

    return area_accum*0.001

# print(1 - normal_cdf(x=100, mu=90, sigma=10))


'''
Normal distr breakout 2
'''
mu = 50
sigma = 15

print(normal_cdf(70, 50, 15) - normal_cdf(50, 50, 15)) # ~0.4088