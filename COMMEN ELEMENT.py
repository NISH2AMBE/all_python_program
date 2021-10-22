# COMMEN NUMBER

def commen_element(l1,l2):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

l3 = [1,2,3,4,5,7,8,9]
l4 = [1,6,1,7,2,4,8,3]

print(commen_element(l3,l4))

