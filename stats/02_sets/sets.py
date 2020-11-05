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

# print(twenty_flips)

'''
How many Heads would you "Expect" in 20 flips?
0.5 * 20 = 10
'''

result_of_heads_20_flips = []

for _ in range(100000):
    result_of_heads_20_flips.append(twenty_flips.count('H'))


print(sum(result_of_heads_20_flips) / 100000)
