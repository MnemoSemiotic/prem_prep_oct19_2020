from random import random

def bernoulli(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

