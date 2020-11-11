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
