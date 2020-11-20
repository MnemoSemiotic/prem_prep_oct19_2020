from random import choice

def get_bit():
    return choice([0,1])


def get_binary(n=8):
    return_list = []

    for _ in range(n):
        return_list.append(get_bit())

    return return_list


def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return float_accum



def get_range(n=8, num_samples=10000):
    high = get_float(n)
    low = get_float(n)

    for _ in range(num_samples):
        flt = get_float(n)

        if flt > high:
            high = flt
        if flt < low:
            low = flt
    
    return low, high

# print(get_range(n=8, num_samples=10000))



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

num_samples=100000
thresh = 0.5
d = sample_from_random_flt(thresh, num_samples)

print(d[f'<= {thresh}'] / num_samples)