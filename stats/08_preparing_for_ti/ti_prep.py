''' TI Style Questions (2020-10-10) '''

'''

TI Skills/Outline

* textbook problems re: Discrete Distrs
    * Recognize and solve problems related to:
        * Binomial
        * Poisson
        * Geometric
        * Uniform
    
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
            * Interpret
'''



'''
Binomial textbook problems

You are sitting on a dock watching boats go by. On average, two out of every 13 boats that goes by has shipping containers on it. What is the probability that, in one particular set of observations, 10 out of 20 boats have shipping containers on them?

p = 2/13
k = 10
n = 20

binomial_pmf(n=20, k=10, p=(2/13) )
'''
def factorial(n):
    prod = 1
    for num in range(1, 1+n):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))


# print(binomial_pmf(n=20, k=10, p=(2/13)))
# 0.000258


'''
you are sitting on a bench holding ten boxes of chocolates. your boxes of chocolates have 7 caramel, 10 coconut, and 5 toffee in each.  what are the odds you pick 10 chocolates from 10 different boxes of chocolates and get 5 caramel filled chocolates?

total_choc = 22
p_caramel = 7/22
k = 5
n = 10
'''
# print(binomial_pmf(n=10, k=5, p=(7/22)))
# 0.121

'''
** watch for keywords: ALL, NONE, AT LEAST/LESS THAN

If on average 20 of 50 counties in California experience wildfires during any given year, what is the prob that all 50 counties will see a wildfire in a single year?
Constraint: massive invisible/fireproof wall betw each county

p = 20/50
n = 50
k = 50
'''
# print(binomial_pmf(n=50, k=50, p=(20/50)))
# print((20/50)**50)
# # 1.2676506002282329e-20



'''
you are at the bus stop and 4 out of every 15 buses that pass by have a subway add, if you watch 30 buses pass by what are the chances that 12 of them will have a subway add?

p = 4/15
n = 30
k = 12
'''
# print(binomial_pmf(n=30, k=12, p=(4/15)))
# 0.042


'''
Walking your dog on any given day, on average 2 out of 5 dogs you pass are golden retrievers. If you see 17 dogs on one particular day, what is the probability that 8 of them are golden retrievers?

p = 2/5
n = 17
k = 8

'''
# print(binomial_pmf(n=17, k=8, p=(2/5)))


'''
You are looking for the stray cats (no name tag cats) in your neighborhood. On average, three out of every 20 cats have no name tags walk through your house. What is the probability that, in one particular set of observations, five no name tag cats out of 10 cats walk by your house?

p = 3/20
n = 10
k = 5
'''

# print(binomial_pmf(n=10, k=5, p=(3/20)))



'''

Poisson textbook problems
'''
from math import e
def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)


'''
Forty stray cats walk by your porch every 2 hours at night. What is the probability that fifty stray cats walk by in 3 hours on a given night?
Constraints: time of night, seasonality, prior cats doesn't affect rate

'''
# lmbda = 60 # 40 * 3/2
# k = 50

# print(poisson_pmf(lmbda, k))
# # 0.023


'''
if on average 3 mosquitos bite you every 30 min while you’re fishing, what is the probability that 7 mosquitos bite you in 3 hours?
'''
# lmbda = 3 * 6
# k = 7
# print(poisson_pmf(lmbda, k))
# # 0.00185

'''
you eat (on avg) 10 chocolates per hour.  what is the probably you eat 20 chocolates in 45 minutes from your 10 boxes of chocolates
'''
# lmbda = 10 * (3/4)
# k = 20
# print(poisson_pmf(lmbda, k))
# # 7.209282379462172e-05


'''
You go for a walk every day at noon. On a 30 minute walk, on avg, you see 3 magpies. If you go for a walk that is an hour and 15 minutes, what is the probably that you will see 11 magpies?
'''
# lmbda = 3 * 2.5
# k = 11
# print(poisson_pmf(lmbda, k))
# # 0.0585

'''
10 dogs are saved from the shelter every 8 hours on average. What is the probability that 25 dogs would be saved in 16 hours?
'''
# lmbda = 10 * 2
# k = 25
# print(poisson_pmf(lmbda, k))
# # ~0.0445

'''
On average, over the course of 365 days there are 300 lightning strikes observed within a particular national forest. Assuming that strikes occur evenly throughout the year, what is the probability that for the month July, there will be more than 50 observed strikes? 
'''
# lmbda = 300 * 31/365
# k_high = 50

# accum = 0.0
# for k in range(0, k_high):
#     accum += poisson_pmf(lmbda, k)
# # print(lmbda)
# print(1 - accum)
# # 1.132522436952943e-05


'''
2 black cars go pass the stop sign every 15min. 
What is the probability that 30 black cars pass by in an hour?
'''
# lmbda = 2*4
# k = 30
# print(poisson_pmf(lmbda, k))
# # 1.5656103352041073e-09



'''

Random Variables

'''

'''
Consider a random variable Z

Z = 0 : when the sum of a 6 sided die and a 36
        sided die is even
Z = 1 : when the sum of a 6 sided die and a 36
        sided die is not even AND is divisible by 3
Z = 2 : in all other circumstances (not Z=0 AND not 
        Z=1) 

What is the probability that three successive dice rolls result in the sequence of outcomes Z=2, Z=1, Z=0
'''

out = []

for i in range(1, 6+1):
    for j in range(1, 36+1):
        sum_ = i + j
        if sum_ % 2 == 0:
            out.append(0)
        elif sum_ % 3 == 0:
            out.append(1)
        else:
            out.append(2)

p_Z_0 = (out.count(0) / len(out))
p_Z_1 = (out.count(1) / len(out))
p_Z_2 = (out.count(2) / len(out))

# print(p_Z_2 * p_Z_1 * p_Z_0)
# # ~0.0278



'''

Coding Mathematical Formulations


'''

'''
A is the result of rolling a 4-sided die 5 times, and processing
it through a function:

sum of each die roll multiplied by 4 over the positional value of that die (indexed starting at 1)

SUM(i=1 to n=5) { roll_i * (4/i) } 

'''

'''                   Using Counting                '''
def roll_math(lst):
    sum_ = 0

    for i, roll in enumerate(lst, 1):
        sum_ += roll * (4 / i)

    return sum_, lst


'''
What is the probability that:

P(A <= 18) = ?

P(A > 12) = ?
'''

outcomes_A = []

for r1 in range(1, 4+1):
    for r2 in range(1, 4+1):
        for r3 in range(1, 4+1):
            for r4 in range(1, 4+1):
                for r5 in range(1, 4+1):
                    outcomes_A.append(roll_math([r1, r2, r3, r4, r5]))

# print(min(outcomes_A))
# print(max(outcomes_A))

le_18 = []
gt_12 = []

for outcome in outcomes_A:
    if outcome[0] <= 18:
        le_18.append(outcome)
    if outcome[0] > 12:
        gt_12.append(outcome)

# print(len(le_18) / len(outcomes_A)) # ~0.21
# print(len(gt_12) / len(outcomes_A)) # ~0.99



'''                   Using Sampling                '''
from random import choice

def roll_die():
    return choice([1,2,3,4])

def roll_die_n_times(n=5):
    rolls = []
    
    for _ in range(n):
        rolls.append(roll_die())

    return rolls


# print(roll_die_n_times(n=5))



'''
Analysis using Dictionaries
'''


'''       Analysis of Counting Approach (5 rolls)            '''

d_counting = dict()

# # count each outcome for a first look
# for outcome in outcomes_A:
#     if outcome not in d:
#         d[outcome] = 0
#     d[outcome] += 1

# for outcome, count in sorted(d.items()):
#     print(f'{outcome}: {count}')

# let's modify this approach to utilize whole number bins

for outcome in outcomes_A:
    k = f'{int(outcome[0])} <= a < {int(outcome[0]) + 1}'

    if k not in d_counting:
        d_counting[k] = [0, []]
    d_counting[k][0] += 1
    d_counting[k][1].append(outcome[1])

# normalize counts to 0:1
for outcome, val in sorted(d_counting.items()):
    d_counting[outcome][0] /= len(outcomes_A) 


for outcome, val in sorted(d_counting.items()):
    print(f'{outcome}: {val[0]}')
    # for lst in val[1]:
    #     print(f'\t{lst}')



'''       Analysis of Sampling Approach (5 rolls)            '''

def analyze_outcomes(n=5, num_samples=10000):
    d = dict()

    for _ in range(num_samples):
        roll_result = roll_die_n_times(n)
        res, roll = roll_math(roll_result)

        k = f'{int(res)} <= a < {int(res) + 1}'

        if k not in d:
            d[k] = [0, []]
        d[k][0] += 1
        d[k][1].append(roll)

    for outcome, val in sorted(d.items()):
        d[outcome][0] /= num_samples

    return d



d_sampling = analyze_outcomes(n=5, num_samples=10000)

for outcome, val in sorted(d_sampling.items()):
    print(f'{outcome}: {val[0]}')
    # for lst in val[1]:
    #     print(f'\t{lst}')