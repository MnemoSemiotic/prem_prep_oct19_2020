'''
Features of a Discrete Random Variable
- countable
- values are "discretized":
    - nothing in between the "discrete" values
    - 0.1, 0.2, 0.3 ... 10.0

Features of a Continuous Random Variable
- measurement problems
    - height of trees, building, etc
    - volume, mass, etc
- potential for infinite precision
    - if we have an infitinely precise instrument, we have "true continuity", an infinite of measurements between any two measurements.

Y_1 is a specific infinitely precise outcome from a continuous distribution with random variable Y. What is the probability of Y_1:  P(Y_1) = ?
0 because an infinitely precise value divided by an infinite number of outcomes is about as close to zero as you can get


in order to get a "specific" probability of a value from a continuous distribution, we in fact define a range.

CDF
to get the Proba of getting less than a given value
can also subtract two cdfs to get the probability of a range of values, thus discretizing our continuous distribution
'''




from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    # return [get_bit for _ in range(n)]
    return_list = []

    for _ in range(n):
        return_list.append(get_bit())
    
    return return_list

# print(get_binary(32))

def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return float_accum

# print(get_float(32))

def get_range(n=8, num_samples=10000):
    high = get_float(n)
    low = get_float(n)

    for _ in range(num_samples):
        flt_high = get_float(n)
        flt_low = get_float(1)

        if flt_high > high:
            high = flt_high
        if flt_low < low:
            low = flt_low
    return low, high

# print(get_range(n=32, num_samples=10000))

'''
Will the upper bound of our range be inclusive or exclusive of 1? Why?
'''


'''
What is the probability of getting a random float of less than 0.752?
'''

def sample_from_random_flt(thresh, num_samples=100000):
    d = dict()

    d[f'<= {thresh}'] = 0
    d[f'> {thresh}'] = 0

    for _ in range(num_samples):
        flt = get_float(32)
        if flt > thresh:
            d[f'> {thresh}'] += 1
        else:
            d[f'<= {thresh}'] += 1

    return d

num_samples = 100000
thresh = 0.752

d = sample_from_random_flt(thresh, num_samples)

print(d[f'<= {thresh}'] / num_samples)