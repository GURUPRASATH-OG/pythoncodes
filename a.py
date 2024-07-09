mark=int(input("enter you mark: "))
if mark<35:
    print("fail")
else:
    print("pass")
cars=('volvo','jaguar','lambo')
i=int(1)
if(i<=len(cars)):
    print(cars[i])
    i=i+1
num=int((input("enter a numeber")))
if(num%3==0 and num%5==0):
    print("the number is both divisible 3 and 5")
elif(num%3==0):
    print("num is divisible by 3 "+str(num))
elif(num%5==0):
    print("num is divisible by 5 "+str(num))
else:
    print("the num is not both divisible 3 and 5 "+str(num))
