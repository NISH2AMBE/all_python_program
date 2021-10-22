# FILTER ODD EVEN

a = int(input("Enter Number :--> "))
z = list(range(1,a))

def filter(l):
    odd_nums = []
    even_nums = []
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]
    return output

print(filter(z))