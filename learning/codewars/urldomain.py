def domain_name(url):
    domain_name = url.replace("/", "").split(".")
    domain_name = ":".join(domain_name).split(":")
    if domain_name[0] == "http" or domain_name[0] == "https":
        domain_name.pop(0)
    if domain_name[0] == "www":
        domain_name.pop(0)
    return domain_name[0]