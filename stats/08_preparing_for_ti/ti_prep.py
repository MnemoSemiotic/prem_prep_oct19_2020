''' TI Style Questions (2020-11-23) '''

'''

TI Skills/Outline

* textbook problems re: Discrete Distrs and Probability
    * Recognize and solve problems related to:
        * Binomial
        * Poisson
        * Geometric
        * Uniform
        * Bayes Theorem

    
    * Understanding counting or binary through the lens of independent trials
        * binary ex: [0,1,1,0,1] <- each "coin flip or bit is independent of the other, if each bit is randomly generated"
        * trinary ex: [0, 1, 1, 2, 0]

    * Coding mathematical formulations

    * Analysis through Dictionaries
        * Pack values into dictionaries
            * Check membership vs not checking membership
        * Transform Dictionary values
        * General analytic approach
            * Create generative process
            * Load results into a dict
            * Interpret/Transform
'''

'''
Binomial Textbook Probs

You are sitting on a park bench watching city buses go by. On average,
two out of every 13 buses that goes by has an advertisement for
oat milk on it. What is the probability that, in one particular
set of observations, 10 out of 20 buses have oat milk ads on them?

p = 2/13
k = 10
n = 20

binomial_pmf(n, k, p)
'''

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))


p = 2/13
k = 10
n = 20

# print(binomial_pmf(n, k, p))


'''
Write your own story problem to be solved with the binomial_pmf
'''