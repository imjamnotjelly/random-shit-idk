def high_and_low(numbers):
    intlist = [int(i) for i in numbers.split()]
    return f"{max(intlist)} {min(intlist)}"