def generate_hashtag(s):
    hlist = "".join([c.capitalize() for c in s.split()])
    return f"#{hlist}" if (len(hlist) > 1 and len(hlist) <= 140) else False