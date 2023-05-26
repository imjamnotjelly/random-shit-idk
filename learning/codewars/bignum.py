def narcissistic(value):
    ntest = 0
    for i in str(value):
        ntest += int(i)**(len(str(value)))
    return ntest == value