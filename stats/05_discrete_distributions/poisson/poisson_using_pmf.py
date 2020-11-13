'''
You have a satellite that takes stellar images of random places in space. On average, each image has 30 stars in it. What is the probability that a given image has 25 stars in it?

e is a constant, a factor of entropy, and it applies in Poisson process
'''
from math import e

def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

def poisson_pmf(lmbda, k):
    return lmbda**k  *  e**(-lmbda) / factorial(k)

print(poisson_pmf(10, 10))