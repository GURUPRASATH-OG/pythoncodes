def student():
    print("enter you informartion")
    mark=int(input("enter you marks: "))
    if(mark>70):
         name=input(("enter your name: "))
         dept=input(("enter you dept: "))
         loc=input(("enter you location: "))
    else:
        print("sorry kiddo you r not elgible")
def loan():
    print("enter salary to check loan eligiblity: ")
    sal=int(input('enter your salary: '))
    age=int(input('enter you age: '))
    if(sal>=20000 or age<=25):
        print(f'your salary is ${sal}  & age is {age}, so your eligible for loan')
        loan=int(input("enter loan amount"))
        if(loan<=50000):
            print("loan granted")
        else:
            print(f'the maximum loan amount is 50000 but you asking {loan}, dont be a greed')
    else:
        print(f'your salary and age is not suitable so not eligible with this ${sal} & {age}')
def userchoie():
    print("hello user!")
    print(f'we have two functions one loan eligibity check and another is student mark function')
    choice=int(input('enter your choice for loan() press 1 and for student() press 2'))
    if(choice==1):
        loan()
    elif(choice==2):
        student()
    else:
        print('enter valid choice either 1 or 2')
userchoie()