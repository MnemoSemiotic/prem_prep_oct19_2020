'''
You have a satellite that takes stellar images of random places in space. On average, each image has 30 stars in it. What is the probability that a given image has 25 stars in it?

e is a constant, a factor of entropy, and it applies in Poisson process


Criteria we need for Poisson:
an average for a given volume/area/length of time
each event needs to be independent
assumption that the rate is consistent, (independent and identical distribution)
'''


from math import e

def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

def poisson_pmf(lmbda, k):
    return lmbda**k  *  e**(-lmbda) / factorial(k)

# print(poisson_pmf(10, 10))


'''
Examples of Poisson-like phenomena

Phenomenon:
Given an area of grass, it is likely that the distribution of pill bugs follows a poisson process.

Question:
PMF: In a square foot of your front yard, on average there are 20 
roly polys in residence. What is the probability that in a given
square foot of your front yard, you find 15 roly polys?

'''
lmbda = 20
k = 15
# print(poisson_pmf(lmbda, k))


'''
Phenomenon:
Cars passing by an intersection at a certain time of day/year, for the duration of a fixed amount of time, will likely follow a Poisson distribution.

Question:
PMF: A given intersection will have on avg 15 cars pass through in 10 minutes.
What is the probability that 20 cars pass through in 15 minutes?
'''
lmbda = 15 * (15/10)
k = 20
# print(poisson_pmf(lmbda, k))

'''
CDF: Given the same intersection, what is the probability that more than 15
cars will pass through in 15 minutes?
'''
proba = 0.0

for k in range(0, 15+1):
    # print(f'{k}: {poisson_pmf(lmbda, k)}')
    proba += poisson_pmf(lmbda, k)

# print(1 - proba)


def poisson_cdf(lmbda, k_high):



