# REAVERCE ALL STRING

def reaverce_eliment(l):
    eliment = []
    for i in l:
        eliment.append(i[::-1])
    return eliment

li = ["nish","123","VIJAY"]
print(reaverce_eliment(li))

