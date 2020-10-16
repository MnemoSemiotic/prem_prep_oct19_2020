from math import e

'''
You have a coin with which you are 2 times more likely to get a heads than a tails. 
h = 2t
h + t = 1
2t + t = 1
3t = 1
t = 1/3

You flip the coin 100 times. 

What is the probability of getting exactly 25 tails?

In [3]: binomial_pmf(100, 25, (1/3))                                                     
Out[3]: 0.017777490475730268
'''




'''
Poisson Distribution
- we need to know an average number of events for a specified "volume" (time, space, or some discrete thing (number of pages))


Examples of Poisson-like phenomena

Phenomenon:
If you take photos from a camera in space, where you randomly aim the camera into space, the distribution of the counts of stars will follow a Poisson distribution.

Question:
PMF: If on average you see 120 stars clearly in a photo taking taken from a satellite, what is the probability of seeing 90 stars in a given photo?

CDF: If on average you see 120 stars clearly in a photo taking taken from a satellite, what is the probability of seeing 90 stars or less in a given photo?


Phenonemon:
Given an area of grass, it is likely that the distribution of pill bugs follows Poisson.

Question:
PMF: In a square foot of your front yard, on average there are 20 roly polys in residence. What is the probability of seeing 15 roly polys in a square foot of your front yard?


Phenomenon:
Cars passing by an intersection at a certain time of day/year for the duration of a fixed amount of time, will likely follow a Poisson distribution.

Question:
A given intersection will on average have 15 cars pass through in 10 minutes. What is the probability that 20 cars pass through in 15 minutes?


Criteria we need for Poisson:
an average for a given volume
each event needs to be independent
assumption that the rate is consistent
'''


'''
Poisson PMF
- given an average (lmbda) number of events for a given volume, get the probability of some number of events for the same or another given volume
'''

''' Factorial '''
def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)

# print(poisson_pmf(10, 10))


'''
Q1
During lunch, 7 people on average walk through a store's front door every 7 minutes.
 What is the probability that 9 people will walk through that door in 7 minutes?

lmbda = 7
k = 9
'''
# print(poisson_pmf(7, 9))

'''
Out of 10000 observations of the given store front, how many of those observations 
would you expect to have 9 people walk through the door?
'''


'''
What is the probability that 12 people walk through the front door in 14 minutes?

lmbda = 14 people
k = 12 people
'''
# print(poisson_pmf(14, 12))


'''
Q2
On average, 20 cars on highway pass by a billboard every 2 minutes during the workday. 

What is the prob that 10 cars pass by in 30 seconds?

lmbda = 5
k = 10
'''
# print(poisson_pmf(5, 10))


'''
CDF:

Prompting question:
If on average 7 mosquitos bite you every 5 minutes while you're fishing, what is the probability that less than 4 mosquitos bite you in 5 minutes?
'''
# print(poisson_pmf(7, 3) + poisson_pmf(7, 2) + poisson_pmf(7, 1) + poisson_pmf(7, 0))

def poisson_cdf(lmbda, high_k):
    cdf = 0.0

    for k in range(high_k+1):
        cdf += poisson_pmf(lmbda, k)
    
    return cdf

# print(poisson_cdf(lmbda=7, high_k=3))


'''
apply a dict to analyze the poisson pmf

keys will be the values of k
the values will be the probabilities associated with that k
'''
def poisson_pmf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lmbda, k)

    return d

d = poisson_pmf_dict(10, 0, 20)

# for k, v in d.items():
#     print(f'{k}: {v}')


def poisson_cdf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_cdf(lmbda, k)

    return d

d = poisson_cdf_dict(10, 0, 20)

# for k, v in d.items():
#     print(f'{k}: {v}')


'''
You are observing a phenomenon that follows perfectly a poisson process.
Given a certain number of observations (10,000), how many events would 
you expect for each value of k, given a lmbda of 10, low_k=0, high_k=30?
'''

def poisson_counts(lmbda, low_k, high_k, num_samples=10000):
    d = dict()

    for k in range(low_k, high_k):
        d[k] = round(poisson_pmf(lmbda, k) * num_samples)

    return d

d = poisson_counts(10, 0, 30, num_samples=100000)

# print(sum(d.values()))

# for k, v in d.items():
#     print(f'{k}: {v / sum(d.values())}')


'''
There's a busy intersection in Denver, on average where 30 cars pass by every 10 minutes. What is the probability that 40 cars will pass by if observing a new ten minute time period?
'''
# print(poisson_pmf(30, 40))


'''
You have a data set from observing a stream where salmon swim by at a rate of 10 fish every 15 minutes. What is the probability that 15 fish swim by in 30 minutes?
'''
# print(poisson_pmf(20, 15))


'''
In a volume of a certain compressed gas that is resampled daily, on average you would expect to observe 20 nitrogenous molecules. What is the probability that you would observe 25 or more of these molecules?
'''
# print(1 - poisson_cdf(20, 24))



'''
random variable A represents the sum of a six-sided die, and a four-sided die

Analyze A
'''

def outcomes_of_A():
    outcomes = []

    for i in range(1, 6+1):
        for j in range(1, 4+1):
            outcomes.append(sum([i, j]))

    return outcomes        


def a_counts_dict():
    d = {}
    outcomes = outcomes_of_A()

    for outcome in outcomes:
        if outcome not in d:
            d[outcome] = 0
        d[outcome] += 1

    return d

# for k, v in a_counts_dict().items():
#     print(f'{k}: {v:}')


def a_proba_dict():
    d = a_counts_dict()
    d_out = dict()

    for k, v in d.items():
        d_out[k] = v / sum(d.values())

    return d_out

# for k, v in a_proba_dict().items():
#     print(f'{k}: {v:}')
