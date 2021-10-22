# FEBONACI

num = int(input("Enter Your Number :-->"))
a = 1
b = 1
c = 0

print(f"{a}\n{b}")
for c in range (1,num):

    c =a + b
    print(f"{c}\t")

    a = b
    b = c
