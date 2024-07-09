#Program to create the calculator.

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
opt=input("Enter the operation which you have to perform=(+,-,*,/)")
if opt=='+':
    sum=num1+num2
    print("Addition of two numbers=",sum)
elif opt=='-':
    sub=num1-num2
    print("Subtraction of two numbers=",sub)
elif opt=='*':
    mul=num1*num2
    print("Multiplication of two numbers=",mul)
elif opt=='/':
    div=num1/num2
    print("Division of two numbers=",div)
else:
    print("Invalid operator")