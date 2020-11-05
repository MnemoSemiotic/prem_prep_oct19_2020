'''
Random Experiment
'''

from random import choice

def coin_flip():
    return choice(['H', 'T'])

print(coin_flip())