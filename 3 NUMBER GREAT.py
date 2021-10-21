# 3 NUMBER GREAT

a = int(input("Enter Your Frist Number :-->"))
b = int(input("Enter Your Second Number :-->"))
c = int(input("Enter Your Third Number :-->"))

if a > b and a > c:
    print(f"Your Frist Number {a} Is Greater")

elif b > a and b > c:
    print(f"Your Second Number {b} Is Greater")

elif c > a and c > b:
    print(f"your Third Number {c} Is Greater")

else:
    print(f"Your all Number {a}  {b}  {c}  Are Same")