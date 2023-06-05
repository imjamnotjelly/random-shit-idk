def move_zeros(lst):
    nlist = [i for i in lst if i != 0]
    nlist.extend([0]*lst.count(0))
    return nlist