# CUBE ROOT

a = int(input ("Enter Your Number For Finding Cube Root :-->"))
b= 1

while b <= a:
    c = b * b * b
    if c == a:
        print(b)
    b= b+1
