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
n = 20 
k = 6 
p = 0.3

# print(binomial_pmf(n, k, p)) # 0.1916


'''
On any weekday morning, a certain bus route has 10 buses in operation. If the probability of any given bus arriving late at a stop is 15% (ha!), and assuming that buses arrive at a given stop independently of each other, what is the likelihood that 2 consecutive buses will arrive late at a given stop?
'''
n = 2
k = 2
p = 0.15

# print(0.15**2) # 0.0225
# print(binomial_pmf(n, k, p)) 


'''What is the likelihood that 2 in 12 buses will arrive late at a given stop?'''
n = 12
k = 2
p = 0.15

# print(binomial_pmf(n, k, p)) # ~0.2924


'''
There are 30 cars in a used car lot. At any given time, there's a 60% chance that each car is working as-is. What is the probability that the 10 cars the dealer sold today are working?
'''
n = 10
k = 10
p = 0.6

# print(p**k) # ~0.006046
# print(binomial_pmf(n, k, p))


'''
you go to chipotle every Tuesday, there’s 14 workers at chipotle and 7 of them work on Tuesdays. whats the chances you’ll see the same worker at the counter 5 out of the next 10 times that you go, if only 3 of them work the counter at any given time?
'''
n = 10
k = 5
p = 3/7

# print(binomial_pmf(n, k, p)) #0.222


'''
In 30 vehicles, it is known that 2 of them will be motorcycles. Knowing this, in 40 vehicles, what is the probability 5 of them will be motorcycles?
'''
n = 40
k = 5
p = 2/30

# print(binomial_pmf(n, k, p)) # ~0.07746


'''
"What is the probability in 12 coin flips of a fair coin, that you get 7 or fewer heads?"
'''
n = 12
p = 0.5
# print(binomial_pmf(n, 7, p) +binomial_pmf(n, 6, p) +binomial_pmf(n, 5, p) +binomial_pmf(n,4 , p) +binomial_pmf(n, 3, p) +binomial_pmf(n, 2, p) +binomial_pmf(n, 1, p) +binomial_pmf(n, 0, p))

# proba = 0.0
# for k in range(0, 7+1):
#     proba += binomial_pmf(n, k, p)

# print(proba)

# print(1 - (binomial_pmf(n, 8, p) + binomial_pmf(n, 9, p) +binomial_pmf(n, 10, p) +binomial_pmf(n, 11, p) +binomial_pmf(n, 12, p)))


'''
CDF
Cumulative Density/Distribution Function
- cumulative implies "accumulator"
'''

def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0.0

    for k in range(0, k_high+1):
        cumulative += binomial_pmf(n, k, p)

    return cumulative

# print(binomial_cdf(12, 7, p=0.5))


'''
"You have 14 components in a circuit. At any given time, there is a 95% chance that a given component is functioning. What is the probability that 12 or more components are functioning? Assume that each component functions independently of every other."
'''
n = 14
p = 0.95
print(binomial_pmf(n, 12, p) + binomial_pmf(n, 13, p) + binomial_pmf(n, 14, p))
print(1 - binomial_cdf(n, 11, p))