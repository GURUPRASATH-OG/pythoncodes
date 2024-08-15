def printline(title):
    box_size=len(title)+4
    print('-'*box_size)
    print('|'+' '*(box_size-2)+'|')
    print('|'+title+'  |')
    print('|'+' '*(box_size-2)+'|')
    print('-'*box_size)

def simplecalculator():
    printline("SIMPLE CALCULATOR")
    
    a=int(input("enter first number:  "))
    b=int(input("enter second number:  "))
    op=input("enter operator symbol like + - * / %:  ")
    if (op =='+'):
       result=a+b
       print(f'addition of {a} and {b} is {result}')
    elif(op=='-'):
       result=a-b
       print(f'substraction of {a} and {b} is {result}')
    elif(op =='*'):
        result=a*b
        print(f'multiplication of {a} and {b} is {result}')
    elif(op=='/'):
         if(b>0):
            result=a/b
            print(f'division of {a} and {b} is {result}')
         else:
            print("division by zero not allowed")
    elif(op=='%'):
        if b!=0:
            result=a%b
            print(f'modulus of {a} and {b} is {result}')
        else:
            print('modulus by zero not allowed')
    else: 
        print("please enter correct operators like + - * / %")   
simplecalculator()