# PALENDROME

def cube(n):
    b = {}
    for i in range(1,n+1):
        e = i**3
        b[i] = e
    return b



b = int(input("Your Number :--> "))
print(cube(b))
