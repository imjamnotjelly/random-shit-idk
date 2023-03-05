from os import system as color_enable
import random

color_enable("")

colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "white": "\033[39m"
}

def cprint(data, color="white"):
    print(colors[color] + str(data) + "\033[0m")

locker_numbers = {
    "jonah":1,
    "micah":2,
    "david":3
}

for n, x in locker_numbers.items():
    template = random.choice([ 
        "x - {} = 3".format(x-3),
        "x + {} = 3".format(3-x),
        "{} - x = 3".format(x+3),
        "x / {} = 3".format(x/3),
        "{} / x = 3".format(3*x),
        "x * {} = 3".format(3/x)
    ])

    cprint(n)
    cprint(template, "yellow")
    cprint(x, "green")

