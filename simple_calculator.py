import math

print("simple calculator")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
while True:
    operation=input("select the operation(1.addition,2.subtraction,3.multiplication,4.division,5.power," \
    "6.modulus,7.square root,8.integer division")
    
    if operation=='1':
        print(num1+num2)
    elif operation=='2':
        print(num1-num2)
    elif operation=="3":
        print(num1*num2)
    elif operation=="4":
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print("can't divisible by zero")   
    elif operation=='5':
        print(num1**num2)
    elif operation=='6':
        print(num1%num2)
    elif operation=='7':
        print(math.sqrt(num1))
    elif operation=='8':
        print(num1//num2)
    else:
        print('invalid')
    
    continue_choice = input("Do you want to continue? (yes/no): ").lower()
    if continue_choice == 'no':
        print("Thank you for using calculator!")
        break        