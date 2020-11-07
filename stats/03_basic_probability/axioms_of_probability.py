setA = set(['bear', 'cat', 'dog', 'dolphin', 'weasel'])
setB = set(['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion'])
setC = set(['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog'])

sample_space = setA.union(setB).union(setC)


'''
Commutative
A U B = B U A
AB = BA
'''
# print(setA.union(setB) == setB.union(setA))
# print(setA.intersection(setB) == setB.intersection(setA))

a = True
b = False
c = True

# print((a or b) == (b or a))
# print((a and b) == (b and a))

'''
Associative
(A U B) U C = A U (B U C)
(AB)C = A(BC)  
'''

# print((setA.union(setB)).union(setC) == (setC.union(setB)).union(setA))

a = True
b = False
c = True

# print(((a or b) or c) == (a or (b or c)))


'''
Distributive 
A U (BC) = (A U B)(A U C)
A(B U C) = (AB) U (AC)
'''

# print(setA.union(setB.intersection(setC)) == (setA.union(setB)).intersection(setA.union(setC)))

# print(a or (b and c) == (a and b) or (a and c))


'''
Idempotent Laws
'''
a = True
b = False
c = True

print((a and a) == a)


'''
Domination Laws
'''
print(setA.intersection(sample_space) == setA)

null_set = set()
print(setA.intersection(null_set) == null_set)


U = {True, False}
A = {True}

print(A.intersection(U) == A)



'''
Absorption Laws
'''

a = True
b = False
c = True

print(a or (a and b) == a)
print(a and ( a or b) == a)


'''
Identity Prop
'''
print(setA.union(null_set) == setA)




'''
Complement Laws
null^c = Universal
Universal^c = null
'''


'''
Involution Law
'''
print(not not a == a)


'''
AB U AB^c == A
'''
print((a and b) or ( a and not b) == a)


'''
DeMorgan's Laws
'''
print((not (a or b)) == ((not a) and (not b)))

print((not (a and b)) == ((not a) or (not b)))