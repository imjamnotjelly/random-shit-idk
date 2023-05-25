# purely mathmatical two number min/max algo

from math import sqrt

def minimum(x, y):
    return (x+y - sqrt((x-y)**2))/2
    
def maximum(x, y):
    return (x+y + sqrt((x-y)**2))/2

test = (-3, 4.232323)
print(minimum(*test))
print(maximum(*test))