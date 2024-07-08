def divide(first, second):
    res = ''
    if second == 0:
        res = 'Ошибка!'
    else:
        res = str(first/second)
    return res

# print(divide(5,0))