from random import random

'''
Bernoulli Trial
'''

def bernoulli(p_success=0.5):
    draw = random()

    if draw < p_success:
        return True
    else:
        return False

# print(bernoulli(0.75))

'''
If you have a coin that on average turns up heads in 90% of its flips, what is the probability that you'll get heads?
0.9
'''

