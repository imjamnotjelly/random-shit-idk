def square_digits(num):
    sd = "".join(str(int(i)**2) for i in str(num))
    return int(sd)