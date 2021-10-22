# FILTER LIST FOR INT

a = [1,3,5,6,'nish',"vijay",1.67,'het',67,True,False]
b = []

for i in a:
    if type(i) == int:
        str(i)
        b.append(i)

    if type(i) == float:
        str(i)
        b.append(i)


print(b)

