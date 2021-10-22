# SUBLIST COUNTER
# date :- 25-1-2021

a = [1,2,3,[5,7,8]]

def counter(l):
    b = 0
    for i in l:
        if type(i) == list:
            b += 1
    return b

print(counter(a))