def move_zeros(lst):
    nlist = [i for i in lst if i != 0]
    for i in range(lst.count(0)):
        nlist.append(0)
    return nlist