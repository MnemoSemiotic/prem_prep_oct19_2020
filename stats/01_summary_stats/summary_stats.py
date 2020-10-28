'''
Mean
'''
def mean(lst, trim_by=0):
    return sum(lst) / len(lst)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

print(mean(a))