def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

# print(factorial(5))

def combinations(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))



'''
PMF: Probability Mass Function
- giving us the probability of a certain specific outcome.
- can answer the binomial question:
- 3 params:
    n : number of trials
    k : represents the number of successes
    p : is the probability of success of a single trial
'''

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

'''
"What is the probability in 12 coin flips of a fair coin, that you get 7 heads?"
'''
# print(binomial_pmf(12, 7, p=0.5)) # 0.193359375


'''
"You have 14 components in a circuit. At any given time, there is a 95% chance that a given component is functioning. What is the probability that 12 components are functioning? Assume that each component functions independently of every other."
'''
# print(binomial_pmf(14, 12, p=0.95)) # 0.1229


'''
You are sitting on a park bench watching geese walk by. There is a probability of 0.3 that any given goose will have feet that are more red than normal. What is the probability that in the next 20 geese you observe, 6 of them will have feet that are more red than usual?
'''
# print(binomial_pmf(20, 6, p=0.3))


'''
On any weekday morning, a certain bus route has 10 buses in operation. If the probability of any given bus arriving late at a stop is 15% (ha!), and assuming that buses arrive at a given stop independently of each other, what is the likelihood that 2 consecutive buses will arrive late at a given stop?
'''
# print(0.15**2)
# print(binomial_pmf(2, 2, p=0.15))

'''What is the likelihood that 2 in 12 buses will arrive late at a given stop?'''
# print(binomial_pmf(12, 2, p=0.15))


'''
There are 30 cars in a used car lot. At any given time, there's a 60% chance that each car is working as-is. What is the probability that the 10 cars the dealer sold today are working?
'''
# Given the constraints:
#   The sale of any given car is not dependent on the person starting the car
#   Time of day/year is irrelevant
# print(0.6**10)
# print(binomial_pmf(10, 10, p=0.60))


'''
you go to chipotle every Tuesday, there’s 14 workers at chipotle and 7 of them work on Tuesdays. whats the chances you’ll see the same worker at the counter 5 out of the next 10 times that you go, if only 3 of them work the counter at any given time?
'''
n = 10
k = 5
p = 3/7
# print(binomial_pmf(10, 5, p=(3/7)))


'''
In 30 vehicles, it is known that 2 of them will be motorcycles. Knowing this, in 40 vehicles, what is the probability 5 of them will be motorcycles?
'''
p = 2/30
n = 40
k = 5
# print(binomial_pmf(n, k, p))


'''
CDF:
Cumulative Density Function
- cumulative implies "accumulator"
'''

'''
"What is the probability in 12 coin flips of a fair coin, that you get 7 or fewer heads?"
'''

# print(binomial_pmf(12, 7, p=0.5) + binomial_pmf(12, 6, p=0.5) + binomial_pmf(12, 5, p=0.5) + binomial_pmf(12, 4, p=0.5) + binomial_pmf(12, 3, p=0.5) + binomial_pmf(12, 2, p=0.5) + binomial_pmf(12, 1, p=0.5) + binomial_pmf(12, 0, p=0.5)) # 0.80615234375


def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0.0

    for k in range(0, k_high+1):
        cumulative += binomial_pmf(n, k, p)

    return cumulative

# print(binomial_cdf(12, 7, p=0.5))


'''
"You have 14 components in a circuit. At any given time, there is a 95% chance that a given component is functioning. What is the probability that 12 or more components are functioning? Assume that each component functions independently of every other."
'''
# print(binomial_pmf(14, 12, 0.95) + binomial_pmf(14, 13, 0.95) + binomial_pmf(14, 14, 0.95))
# print(1 - binomial_cdf(14, 11, 0.95))



'''There are 8 components in parallel and at least 3 of those components need to be operational for a circuit to function. The probability of any given component being operational is 0.7. What is the probability that 3 components are operational?'''


# print(binomial_pmf(8, 3, p=0.7))


'''What is the probability that at least 3 components are operational?'''

# P(X = 3) + P(X = 4) ... P(X = 8)
# print(binomial_pmf(8, 3, p=0.7)+binomial_pmf(8, 4, p=0.7)+binomial_pmf(8, 5, p=0.7)+binomial_pmf(8, 6, p=0.7)+binomial_pmf(8, 7, p=0.7)+binomial_pmf(8, 8, p=0.7))

# print(1 - (binomial_pmf(8, 2, p=0.7)+binomial_pmf(8, 1, p=0.7+binomial_pmf(8, 0, p=0.7))))

# print(1 - binomial_cdf(8, 2, p=0.7))

# for k, v in binomial_dict(8, 0, 8, p=0.7).items():
#     print(f'{k}: {v}')



'''
Suppose you independently flip a coin 5 times and the outcome of each toss is equally probable for a heads or a tails. What is the probability of obtaining exactly 2 tails?
'''
# print(binomial_pmf(5, 2))


'''
Suppose you are building some sort of machine that relies on a specific component. The component is very delicate and the probability of it failing is 0.32. You decide to install 3 of these components in parallel, such that they are independent to each other, to ensure that you only need 1 to work to get your machine working. 
'''
# # What is the probability that exactly 1 of these components work?
# p = 1 - 0.32
# k = 1
# n = 3

# print(binomial_pmf(n, k, p))

# # What is the probability that 1 or more of these components work?
# print(binomial_pmf(n, 1, p) + binomial_pmf(n, 2, p) + binomial_pmf(n, 3, p))
# print(1 - binomial_pmf(n, 0, p))


def binomial_pmf_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, k, p)
    
    return d

for k, v in binomial_pmf_dict(12, 0, 12, p=0.25).items():
    print(f'{k}: {v}')