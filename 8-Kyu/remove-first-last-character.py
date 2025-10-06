def remove_char(s):
    if len(s) == 2:
        return ''
    else:
        arr = list(s)
        arr.pop(0)
        arr.pop(-1)
        s = "".join(arr)
        return s