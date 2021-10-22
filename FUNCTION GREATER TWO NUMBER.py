#FUNCTION GREATER TWO NUMBER

def two_number(a,b):
    if a>b:
        return "Frist Number Is Greater"
    elif b>a:
        return "Second Number Is Greater"
    else:
        return f"Frist Number {a} and Second Number {b} Are Same"

c = int(input("Enter Frist Number :-->"))
d = int(input("Enter Second Number :-->"))
e =two_number(c,d)
print(e)