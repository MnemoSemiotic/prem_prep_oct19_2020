from random import random


def bernoulli(p=0.5):
    if random() < p:
        return 1
    else:
        return 0


def perform_geometric(p=0.5):
    num_trials = 0
    for _ in range(2000000):
        flip = bernoulli(p)
        num_trials += 1

        print(f'trial: {flip}')
        if flip == 1:
            break

    print(f'Success on the {num_trials} trial!')

p=0.00005
perform_geometric(p)
print(f'Expectation is {(1)/p} for a probability of {p}')