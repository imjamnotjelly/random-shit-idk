from math import sqrt

def ab_v(x):
    return sqrt(x**2)
    
def ab_d(x, y):
    return ab_v(x - y)
    
def mean(x, y):
    return (x + y)/2

def minimum(x, y):
    return mean(x, y) - ab_d(x, y)/2

def maximum(x, y):
    return mean(x, y) + ab_d(x, y)/2

test = [8, 4]

print(minimum(*test))

print(maximum(*test))
