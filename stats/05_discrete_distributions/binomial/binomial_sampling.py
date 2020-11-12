from random import choice, random

'''
using choice we are limited to a fixed p value
'''

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    lst = []
    for _ in range(n):
        lst.append(get_bit())

    return lst

print(generate_n_bits(n=16))