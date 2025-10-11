def get_middle(s):
    n = len(s)
    mid = n // 2
    return s[mid - 1:mid + 1] if n % 2 == 0 else s[mid]
