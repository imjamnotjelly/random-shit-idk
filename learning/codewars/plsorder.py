def order(sentence):
    reorder = sentence.split()
    for i in sentence.split():
        for c in i:
            if c.isdigit():
                reorder[int(c)-1] = i
    return " ".join(reorder)