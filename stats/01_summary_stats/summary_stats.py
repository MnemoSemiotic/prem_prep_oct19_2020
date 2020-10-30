'''
Mean
'''
def mean(lst, trim_by=0):
    lst_ = lst.copy()

    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by:-trim_by]

    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim_by=1))


'''
Breakout Slide 10

An article published in the journal, Indoor Air, considered two different air samples to test for endotoxin concentrations, the first in urban households, and the second in farmhouses.
'''
urban =  [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

'''
A. Determine the sample mean for each group.
'''
# print(f'Sample Mean Urban: {round(mean(urban), 1)}')
# print(f'Sample Mean Farmhouse: {round(mean(farmhouse), 1)}')

'''
B. Determine the trimmed mean for each group by trimming the smallest and largest value from each group.
'''

# print(f'Sample Trimmed Mean Urban: {round(mean(urban, trim_by=1), 1)}')
# print(f'Sample Trimmed Mean Farmhouse: {round(mean(farmhouse,trim_by=1), 1)}')


'''
Median
'''

def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        return lst_sorted[int(len(lst)/2)]
    # if even
    else:
        upper_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_idx - 1], lst_sorted[upper_idx]])


odd = [13, 18, 13, 14, 13, 16, 14, 21, 13]
even = [15, 14, 10, 8, 12, 8, 16, 13]

# print(sorted(odd))
# print(median(odd))

# print(sorted(even))
# print(median(even))


'''
An article published in the journal, Indoor Air, considered two different air samples to test for endotoxin concentrations, the first in urban households, and the second in farmhouses.

Calculate the Median of both groups

'''
urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0]

# print(sorted(urban))
# print(f'Median Urban: {round(median(urban), 1)}')
# print(sorted(farmhouse))
# print(f'Median Farmhouse: {round(median(farmhouse), 1)}')


'''
Breakout Slide 18

An issue of a recent magazine reported the following home sale amounts for a sample of homes in Alameda, CA, all of which were sold in the previous month (1000s of $):

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }

Find the mean value of the homes sold in April

Find the median value of the homes sold in April 

Do you think mean or median is a “better” measure of center for this data? why? 

'''
house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(sorted(house_prices))
# print(f'Mean House Price: {round(mean(house_prices), 3)}')
# print(f'Median House Price: {round(median(house_prices), 3)}')


'''
Mode
'''
def mode(lst):
    most_occurring = lst[0]

    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring

mode_lst = ['skiing', 'kayaking', 'climbing', 'climbing', 'climbing', 'kayaking', 'juggles', 'kayaking', 'macromet']

# print(mode(mode_lst))



'''
Five-Number Summary
Interquartile Range
Detect Outliers
'''
def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)

    sorted_lst = sorted(lst)

    if len(lst) % 2 == 1:
        lower_half = sorted_lst[0: int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2)+1: ]
    else:
        lower_half = sorted_lst[0: int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2): ]

    q1 = median(lower_half)
    q3 = median(upper_half)


    return min_, q1, med, q3, max_

a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]

# print(sorted(a))
# print(five_number_summary(a))
# print('\n')
# print(sorted(b))
# print(five_number_summary(b))


'''
IQR : Interquartile Range
Q3 - Q1
'''
def iqr(lst):
    _, q1, _, q3, _ = five_number_summary(lst)

    return q3 - q1


a = list(range(0,50+1, 5))
b = list(range(0, 100+1, 5))

# print(a)
# print(five_number_summary(a))
# print(iqr(a))

# print(b)
# print(five_number_summary(b))
# print(iqr(b))


'''
Detect Outliers
low outliers < Q1 - IQR*1.5
high outliers > Q3 + IQR*1.5
'''

def detect_outliers(lst, outlier_coef=1.5):
    '''
    returns a list of the outliers found in the data
    '''
    _, q1, _, q3, _ = five_number_summary(lst)
    iqr_ = iqr(lst)

    outliers = []

    for num in lst:
        if num < q1 - outlier_coef*iqr_:
            outliers.append(num)

        if num > q3 + outlier_coef*iqr_:
            outliers.append(num)

    return outliers


'''
Breakout Slide 30

Consider the dataset from the previous question:
A = { 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }


'''

# house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(sorted(house_prices))

# # Calculate the five number summary for the data
# # mean = 620.5 
# # median = 582.5

# print(five_number_summary(house_prices))

# # Determine the IQR of the Dataset
# print(iqr(house_prices))

# # Determine whether any of the data points can be defined as outliers. If so, what are the outliers?
# print(detect_outliers(house_prices, outlier_coef=1.5))

# # What is the best measure of centrality for this data?
# # median

# print(mean([408, 540, 555, 575, 590, 608, 615, 679]))


'''
Breakout Slide 32

Consider the dataset:
'''

# a = [18, 15, 7, 27, 2, 9, 12, 1, 6, 19, 5]

# print(sorted(a))
# # Calculate the five number summary for the data
# print(five_number_summary(a))

# # Determine the IQR of the Dataset
# print(iqr(a))

# # Determine whether any of the data points can be defined as outliers. If so, what are the outliers?
# print(detect_outliers(a))

# # What is the best measure of centrality for this data?
# print(f'mean: {mean(a)}')
# print(f'median: {median(a)}')


'''
Write a function called remove_outliers, that takes a list and returns a copy of that list with the outliers removed.
Be sure to include an outlier_coef and default that value to 1.5
'''
def remove_outliers(lst, outlier_coef=1.5):
    outliers = detect_outliers(lst, outlier_coef)
    output = []

    for num in lst:
        if num not in outliers:
            output.append(num)

    return output

house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(remove_outliers(house_prices))

'''
Variance (sigma^2 or s^2)

Standard Deviation (sigma, or s)

roughly: the average distance betw each data value and the mean

Bessel's correction (instead of dividing by n for a population, divide by n-1 for a sample)
'''
def variance(lst, sample=True):
    mean_ = mean(lst)

    total = 0

    for item in lst:
        total += (item - mean_)**2

    if sample:
        return total / (len(lst) - 1)
    else:
        return total / len(lst)

from math import sqrt
def stdev(lst, sample=True):
    return sqrt(variance(lst, sample))

'''
Breakout Slide 41

An issue of a recent magazine reported the following home sale amounts for a sample of homes in Alameda, CA, all of which were sold in the previous month (1000s of $) (use the sample calculations):

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }

Find the variance of the homes sold in April

Find the standard deviation of the homes sold in April 

If we exclude the values we considered to be outliers, do you think the variance will increase or decrease? Check your answer by making the calculation.

'''

house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

print(sorted(house_prices))
print(f'Samp Variance: {variance(house_prices, sample=True)}')
print(f'Pop Variance: {variance(house_prices, sample=False)}')
print(f'Samp StDev: {stdev(house_prices, sample=True)}')
print(f'Pop StDev: {stdev(house_prices, sample=False)}')