# recursive min/max func generator (very lag!!!)

from math import sqrt
from random import uniform

def minimum(*nums):
    if len(nums) > 2:
        x = minimum(*nums[:-1])
        y = nums[-1]
    else:
        x, y = nums
    return f"({x}+{y}-sqrt(({x}-{y})**2))/2"

def maximum(*nums):
    if len(nums) > 2:
        x = maximum(*nums[:-1])
        y = nums[-1]
    else:
        x, y = nums
    return f"({x}+{y}+sqrt(({x}-{y})**2))/2" # yeah yeah im aware that theres no abstraction

nrange = lambda x:tuple(range(1, x+1))
rrange = lambda mn, mx, amt:tuple(uniform(mn, mx) for _ in range(amt))

test = rrange(1, 10, 5)
print(test)

min_func = minimum(*test)
max_func = maximum(*test)
print(min_func, eval(min_func))
print(max_func, eval(max_func))
