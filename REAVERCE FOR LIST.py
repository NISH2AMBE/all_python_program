# REAVERCE FOR LIST

def reaverce(l):
    numbers = []
    for i in range(len(l)):
        a= l.pop()
        numbers.append(a)
    return numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
print(reaverce(numbers))
