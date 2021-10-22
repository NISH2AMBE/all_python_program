# PASSWORD MAKER
# DATE :- 4 - 2 - 2021

import random

cod2 = str(random.randint(101,999))

a = input("Enter Your Name :--> ")
b = input("Enter Your Mobile Number :--> ")

c = a[:3]
d = b[5:7:]
e = cod2
f = c+e+d
print("Your Password Is :--> {}".format(f))