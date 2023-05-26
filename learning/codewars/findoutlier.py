def find_outlier(integers):
    ltype = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            ltype += 1
    for i in integers:
        if (ltype > 1 and i % 2 != 0) or (ltype <= 1 and i % 2 == 0):
            return i