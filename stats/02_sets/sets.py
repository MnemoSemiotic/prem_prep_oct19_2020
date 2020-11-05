'''
Random Experiment
'''

from random import choice

def coin_flip():
    return choice(['H', 'T'])

# print(coin_flip())

# 20 flips
twenty_flips = []

for _ in range(20):
    twenty_flips.append(coin_flip())

print(twenty_flips)