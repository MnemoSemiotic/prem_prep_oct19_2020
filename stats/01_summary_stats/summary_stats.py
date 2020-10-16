'''
Mean
'''

def mean(lst, trim_by=0):
    lst_ = lst.copy()
    
    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by:-trim_by]
        print(lst_)
    return sum(lst_) / len(lst_)

# a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim_by=1))



'''
Median
'''
lst1_odd = [13, 18, 13, 14, 13, 16, 14, 21, 13]
lst2_even = [15, 14, 10, 8, 12, 8, 16, 13]



def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        return lst_sorted[int(len(lst) / 2)]
    # if even
    else:
        upper_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_idx - 1], 
                     lst_sorted[upper_idx]])

# print(sorted(lst1_odd))
# print(median(lst1_odd))

# print()

# print(sorted(lst2_even))
# print(median(lst2_even))


'''
Housing Prices Breakout

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }

Find the mean value of the homes sold in April

Find the median value of the homes sold in April 

Do you think mean or median is a “better” measure of center for this data? why? 

'''

house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(sorted(house_prices))

# print(f'mean {mean(house_prices)}')
# print(f'median {median(house_prices)}')


'''
Mode
'''

def mode(lst):
    most_occurring = lst[0]

    for item in lst[0:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring

mode_lst = ['writing', 'writing', 'hiking', 'painting', 'skating', 'skating', 'writing', 'macromet']

# print(mode(mode_lst))



'''
Five Number Summary
Interquartile Range
Detect Outliers
'''

def five_num_summary(lst):
    min_ = min(lst)
    max_ = max(lst)

    med = median(lst)

    sorted_lst = sorted(lst)

    # print(sorted_lst)

    if len(lst) % 2 == 1:
        # [[1, 2, 5, 6, 7], 9, [12, 15, 18, 19, 27]]
        #  
        lower_half = sorted_lst[0: int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2)+1:]
        
    else:
        # [[1, 4, 6, 7, 10, 14, 16,] [22, 24, 46, 48, 51, 54, 56]]
        #  0                   6+1 6+1                     
        lower_half = sorted_lst[0:int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2):]

    # print(lower_half)
    # print(upper_half)
    q1 = median(lower_half)
    q3 = median(upper_half)

    return min_, q1, med, q3, max_

a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]

# print(five_num_summary(a))
# print(five_num_summary(b))


''' Interquartile Range '''

def iqr(lst):
    _, q1, _, q3, _ = five_num_summary(lst)
    return q3 - q1

# print(iqr(a))
# print(iqr(b))


''' Detect Outlier '''

def detect_outliers(lst, outlier_coef=1.5):
    _, q1, _, q3, _ = five_num_summary(lst)
    iqr_ = iqr(lst)

    outliers = []

    for num in lst:
        if num < q1 - outlier_coef*iqr_:
            outliers.append(num)
        if num > q3 + outlier_coef*iqr_:
            outliers.append(num)

    return outliers

house_values = [-6000000, 450000, 652234, 89000, 750000, 224968, 500000, 125000, 36000, 70000, 650000, 3400000, 560000]


# print(detect_outliers(house_values))
# [-6000000, 3400000]


'''
Write a function called remove_outliers, that takes a list and returns a list with the outliers removed.
'''

def remove_outliers(lst):
    outliers = detect_outliers(lst)
    output = []

    for num in lst:
        if num not in outliers:
            output.append(num)
    
    return output


# print(remove_outliers(house_values))


'''
Variance and Standard Deviation

'''

def variance(lst, sample=True):
    total = 0

    mean_ = mean(lst)

    for item in lst:
        total += (item - mean_)**2

    if sample:
        return total / (len(lst) - 1)
    else:
        return total / len(lst)


from math import sqrt
def stdev(lst, sample=True):
    return sqrt(variance(lst, sample))


a = [1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27]
# print(mean(a))

# print(f'Pop: {variance(a, sample=False)}')
# print(f'Sample: {variance(a, sample=True)}')


# from random import choice

# pop = list(range(0,1000))

# samp = []

# while len(samp) < 200:
#     num = choice(range(0,1000))
#     if num not in samp:
#         samp.append(num)



# print('Population')
# print(f'mu: {mean(pop)}')
# print(f'sigma^2: {variance(pop)}')
# print(f'sigma: {stdev(pop)}')

# print()

# print('Sample')
# print(f'x_bar: {mean(samp)}')
# print(f's^2: {variance(samp)}')
# print(f's: {stdev(samp)}')


'''
Breakout Slide 41
'''

house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# a.
print(f'sample variance: {variance(house_prices)}')

# b. 
print(f'sample stdev: {stdev(house_prices)}')

# c. 
print(f'sample variance: {variance(remove_outliers(house_prices))}')


# sample variance: 64140.72222222222
# sample stdev: 253.2601868083932
# sample variance: 2112.285714285714