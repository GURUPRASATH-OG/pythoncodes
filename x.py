def ab():
    odd=0
    even=0
    a=int(input("start of the loop"))
    b=int(input("end of the loop"))
    for i in range(a,b):
        if (i%2==0):
            print(i)
            even=even+1
        elif(i%2!=0):
            odd=odd+1
    print(f'sum of odd number between {a} and {b} is {odd}')  
    print(f'sum of even number between {a} and {b} is {even}')       
#ab()
def div():
    count=0
    a=int(input())
    b=int(input())
    for i in range(a,b):
        if(i%3==0 and i%5==0):
            count=count+1
    print(f' sum of num divisble by 3 and 5 from {a} to  {b} is: {count}')
#div()
#sum of five natural numbers
def nat_sum():
    count=0
    st=int(input())
    en=int(input())
    for i in range(st,en):
        if(i>0):
            count=i+count
            print(i)
    print(count)
#nat_sum()
#sum and avg of ten user inputs
def big():
    avg=0
    total=0
    for i in range(1,11):
        num=int(input())
        total=total+num
        avg=total/10
    print(f'the sum: {total} and average is {int(avg)}')
#big()
# nterms of the natural number and thier sum
def n():
    count=0
    a=int(input('start'))
    b=int(input('end'))
    for i in range(a,b):
        if(i>0):
            count=count+i
            print(i)
    print(f'sum of n natural numbers {count}')
#n()
#to display cube of number
def cube():
    cube=0
    a=int(input('no of terms'))
    for i in range(1,a):
        cube=i*i*i
        print(f'Number is: {i} and the cube of the {i} is: {cube}')
#cube()
#getting inputs and printing avg and sum using the list concept
def sumlist():
    tot=0
    avg=0
    for i in range(1,11):
        num=[]
        num.append(int(input()))
        for i in num:
            tot=tot+i
            avg=tot/10
    print(f'the sum is{tot} and avg is{avg}')
#sumlist()
# print the week days
def week():
    a=int(input())
    for i in range(1,a):
        print(f'week:{i}')
        for j in range(i):
            
            print('day'+str(j))
#week()

def asterik():
    a=int(input('enter range'))
    for i in range(1,a):
        print()
        for j in range(1,i+1):
            print('*',end=' ')
#asterik()
#while loop exercises
def wh():
    a=int(input())
    i=10
    while(i>0):
        print(i)
        i=i-1
#wh()
#factorial of a number
def fact():
    fact=1
    a=int(input())
    while(a>0):
        fact=fact*a
        a=a-1
    print(fact)
#fact()
#list 
a=['volvo','bmw','porsche','audi']
for i in a:
    print(i)
 
print(a)
b={
    "name":"sam",
     "age":3,
     "location":"chennai",
     "state":"tamil nadu",
     "qualification":[10,12,"UG"]
}
print(b.values())
b.update({"name":"santhosh"})
b.pop("location")
#print(b)
#tuples
#t=('poda','venna','venna','poda')
#print(t[0])
#function passing argument
s=0
def arg(a,b):
    s=a+b
    print(s)
    if(a%2==0):
        print("is even")
    else:
        print("is odd")
    
#arg(11 ,20)
def ra(a,b):
    values=[]
    for i in range(a,b):
        values.append(i)
    return values
#a=int(input())
#b=int(input())
#c=ra(a,b)
#print(c)
#user validation
def validate_user(u_name,u_passwd):
    un=input('enter your user name: ')
    pw=input('enter you passwd: ')
    if(u_name==un and u_passwd==pw):
        #print(f'welcome onboard, {u_name}')
        return True
    else:
        return False
        #print(f'{u_name},Bastard enter the correct credentials')
#a=input('set your username: ')
#b=input('set your password: ')
#c=validate_user(a,b)
#print(c)
# sum function using return
"""a=int(input())
b=int(input())
c=int(input())
su=0
def sumof(a,b):
    su=a+b
    su=su*c
    return su"""
#ans=sumof(a,b)
#print(ans)
#laptop calss
class laptop:
    def __init__():
        price=int()
        processor="i3"
        ram="8gb"
    def specs(self):
        print(price,ram,processor)
hp=laptop()
hp.price=56000
hp.processor="i5"
hp.ram="16gb"
hp.laptop()
    



    

