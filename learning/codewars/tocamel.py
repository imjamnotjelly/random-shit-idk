def to_camel_case(text):
    termlist = text.replace("_", "-").split("-")
    for i in range(1, len(termlist)):
        termlist[i] = termlist[i].capitalize()
    return "".join(termlist)