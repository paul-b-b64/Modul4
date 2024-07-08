def divide(first, second):
    res = ''
    if second == 0:
        from math import inf
        res = inf
    else:
        res = str(first/second)
    return res
