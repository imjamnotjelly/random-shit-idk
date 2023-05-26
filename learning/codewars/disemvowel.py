def disemvowel(string_):
    return "".join(i for i in string_ if i.lower() not in "aeiou")