from geometric_using_pmf import *

'''
Geometric Breakout 1
Suppose you have an unfair coin, with a 68% chance of getting tails. 
What is the probability that the first head will be on the 3rd trial?
'''

# print(geometric_pmf(p=0.32, k=3, inclusive=True))

'''
Geometric Breakout 2
According to the article “Characterizing the Severity and Risk of Drought in the Poudre River, Colorado” taken from a water conservation journal, the drought length Y is the number of consecutive time intervals in which the water supply remains below a critical value y0 (a deficit), preceded by and followed by periods in which the supply exceeds this critical value (a surplus). The journal proposes a geometric distribution with  p = 0.409 for this random variable.
(hint: consider the probability p to represent the “success” of breaking a drought)
What is the probability that the drought lasts exactly three intervals?
'''

'''
Given that there is a drought, what is the probability that the drought lasts at most three intervals?
'''




'''
Differentiating Binomial, Poisson, Geometric, and basic probability
'''
# Binomial
# What is the probability that some number out of some number of events is successful?

# p=0.7, n_trial = 5, what is the proba that 3 of the 5 trials are successful?


# Poisson
# On average, some number of events happens in this volume (of time, space, etc). 

# What is the probability of some (other) number of events happens in this volume or 
# some expansion/contraction of this volume?
# On avg 14 events occur in 5 minutes, what is the probability that 20 events occur 
# in 8 minutes?


# Geometric
# The proba of some binary event is p. What is the probability of having your first
# success on the nth trial?

# The p of success is 0.21. What is the probability of having 4 failures before the
# first success?


# Basic Probability
# The probability of some event is p_0. The probability of another, independent event is p_1
# What is the probability of both events occurring? p_0 * p_1

# The probability of getting heads on a certain coin is 0.83. What is the probability of 
# getting 0 heads in 5 flips? 
print(0.17**5) # ~ 0.000142

# What is the probability of getting at least one heads in 5 flips?
print(1 - 0.17**5)

# 00000 <-- all failures

# 00001 <-- everything else
# 00010
# 00011
# ...
# 11111



# for some more review:
#   https://www.statlect.com/probability-distributions/
#   https://www.jbstatistics.com/