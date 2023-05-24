from math import sqrt

def minimum(x, y):
    return(x+y)/2 - sqrt((x-y)**2)/2
    
def maximum(x, y):
    return (x+y)/2 + sqrt((x-y)**2)/2

test = (8, 4)
print(minimum(*test))
print(maximum(*test))
