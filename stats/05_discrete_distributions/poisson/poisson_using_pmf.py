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
    cdf = 0.0

    for k in range(k_high+1):
        cdf += poisson_pmf(lmbda, k)

    return cdf

# print(1 - poisson_cdf(lmbda, 15))


'''
During lunch, 7 people on average walk through a store's front door every 7 minutes.
 What is the probability that 9 people will walk through that door in 7 minutes?
lmbda = 7
k = 9
'''
# print(poisson_pmf(7, 9))


'''
What is the probability that 12 people walk through the front door in 14 minutes?

'''
lmbda = 14
k = 12
# print(poisson_pmf(lmbda, k))


'''
On average, 20 cars on a highway pass by a billboard every 2 minutes during the workday. 
What is the prob that 10 cars pass by in 30 seconds?
'''
lmbda = 5
k = 10
# print(poisson_pmf(lmbda, k))


'''
If on average 7 mosquitos bite you every 5 minutes while you're fishing, what is the probability that less than 4 mosquitos bite you in 5 minutes?
'''
lmbda = 7
k_high = 3

# print(poisson_pmf(7, 3) + poisson_pmf(7, 2) + poisson_pmf(7, 1) + poisson_pmf(7, 0))
# print(poisson_cdf(lmbda, k_high))



'''

apply a dict to analyze the poisson pmf

keys will be the values of k
value will be the probabilities associated with k outcomes
'''

def poisson_pmf_dict(lmbda, low_k, high_k):
    pass



