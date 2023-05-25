# fuck this shit it no workey ;(

def manumeral(num):
    def digit_diff(x=2, y=1):
        return sum([int(d) for d in str(num*x)]) - sum([int(d) for d in str(num*y)])
    values = [digit_diff(3), digit_diff()]
    values = {abs(n):n for n in values}
    return values[min(values.keys())]

print(", ".join([str(manumeral(i)) for i in range(1, 10)]))