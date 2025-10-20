# return masked string
def maskify(cc):
    masked = "#" * (len(cc) - 4) + cc[-4:]
    return masked
