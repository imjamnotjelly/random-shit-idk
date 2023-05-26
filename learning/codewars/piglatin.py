def pig_it(text):
    pl = text.split()
    return " ".join(f"{i[1:]}{i[0]}ay" if i.isalpha() else i for i in pl)