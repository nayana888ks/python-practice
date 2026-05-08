#Simple Calculator Using match
num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
print("1,Addition","2,Substraction","3,multiplication","4,division")
operation=int(input("enter the operation"))
match operation:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
      print(num1*num2)
    case 4:
     print(num1/num2)
    case _ :
     print("none")
     
#Traffic Light System
print("1,red","2,yellow","3,green")
color=int(input("enter the colour"))
match color:
   case 1:
      print("the color is red ,you have to stop")
   case 2:
      print("the color is yellow,you have to wait")
   case 3:
       print("the color is green,you can go")
   case _:
      print("invalid choice") 