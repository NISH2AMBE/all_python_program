# LOAN CALCULATION

p = int(input("Enter Your Amount :-->"))
r = float(input("Enter Your Rate :-->"))
t = int(input("Enter Your Time (Year) :-->"))

i = p * r * t/100
a = p + i
print("****************************")
print(f"Your Interest Is :-->{i}")
print("****************************")

print(f"Your Total Amount Is :--> {a}")
print("****************************")