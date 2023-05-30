# recursive min/max func generator (very lag!!!)

from math import sqrt

def minimum(*nums):
    if len(nums) > 2:
        x = minimum(*nums[:-1])
        y = nums[-1]
    else:
        x, y = nums
    return f"({x}+{y}-sqrt(({x}-{y})**2))/2"

def maximum(*nums):
    if len(nums) > 2:
        x = minimum(*nums[:-1])
        y = nums[-1]
    else:
        x, y = nums
    return f"({x}+{y}+sqrt(({x}-{y})**2))/2" # yeah yeah im aware that theres no abstraction

nrange = lambda x:tuple(range(1, x+1))
test = nrange(20)

min_func = minimum(*test)
max_func = maximum(*test)
print(min_func, eval(min_func))
print(max_func, eval(max_func))
