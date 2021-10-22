# SQURE IN LIST

numbers = list(range(1,11))

def squre(l):
    number = []
    for i in l:
        number.append(i**2)
    return number


print(squre(numbers))