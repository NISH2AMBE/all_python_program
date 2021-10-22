# PALENDROME

def ulta(a):
    b = a[-1::-1]
    if a == b:
        print(True)
    else:
        print(False)

c = input("Enter Name:--> ")


print(ulta(c))
