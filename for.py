dob=int(input("Enter your date of birth: "))
i=int(dob)
age=int(0)
for i in range(i,2024):
    age +=1
print(f'your age is {age}')

def table():
    print("this function will print multiplication table")
    i=int(1)
    n=int(input("enter table number: "))
    rang=int(input("enter range: "))
    for i in range(i,rang):
        pro=i*n
        print(f'{n}x{i}={pro}')
table()