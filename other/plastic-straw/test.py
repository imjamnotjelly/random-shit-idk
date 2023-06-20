from turtle import *

"""
class Button:
    def __init__(self, x, y, width, height, **kwargs):
        self.x = x
        self.y = y
        self.anchor = kwargs.get("anchor", "center")

def oc_test(*args):
    print(args)

screen = getscreen()
screen.onclick(oc_test)
"""

def index_cdn(iterable, condition, default=-1):
    for i, v in enumerate(iterable):
        if condition(v):
            return i
    return default

def insert(string, index, char):
    return string[:index] + char + string[index:]

def rect(width, height, radius=0):
    dim = (width, height)
    if isinstance(radius, str):
        l_index = index_cdn(radius, str.isalpha)
        radius = eval(insert(radius, l_index, "*"))
    radius = min(radius, min(dim)/2)
    for turn in range(4):
        fd(dim[turn%2]-radius*2)
        circle(radius, 90)
pu()
rect(300, 100, "1/8 min(dim)")
pd()
done()