# USER INFO

user = {}

a = input("What Your Name :--> ")
b = input("What Your Age :--> ")
c = input("What Your Father Name :--> ")

print("-------------------------")
user['name'] = a
user['Age'] = b
user['Father Name'] = c


for i,j in user.items():
    print(f"{i} : {j}")