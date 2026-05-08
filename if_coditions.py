#if number is a positive
a=int(input("enter the number."))
if a>0:
    print("the number is positive")
else:
    print("the number is negative")

#Check if a given number is divisible by 5.
num=int(input("enter the number"))
if num%5==0:
    print("number is divisible by 5")
else:
    print("it is not")

#Take a string input and print "Empty string" if its length is 0.
info=str(input("enter the string\t"))
if len(info)==0:
    print("empty string")
else:
    print("string has value")

 #or
""" if not info: print("empty string") """


#Take a number and check whether it is greater than 100 or not.
num=int(input("enter the number"))
if num>100:
    print("nureater than 100")
else:
    print("not greater than 100")


#Check if a character is a vowel or not.
data=("enter the character")
if data.lower() in ['a','e','i','o','u']:
  print("its a vowel") 
else: 
    print("its not a vowel")

#or
"""if data.lower() in "aeiou":
"""

#check wether the year is a year
year=int(input("enter a year"))
if year%4==0 and year%100!=0:
    print("it's a leap year")
elif year%400==0:
    print("its a leap year")
else:
    print("its not a leap year")


#logical operators

#Check if a numbeen 10 and 50.
data=int(input("enter the number"))
if 10<data<50:
    print("the number is between the 10 and 50")
else:
    print("it's not")

#Write a program that checks:If username is "admin"  AND password is "1234"
name=str(input("enter the username"))
password=int(input("enter the password"))
if name=="admin" and password==1234 :  
    print("user allowed")
else:
    print("user not allowed")

#Take age and check:
age=int(input("enter your age"))
if age<5:
    print("toddler")
elif age>10: 
    print("it's a child")
elif 11<age<20:
    print("its a teenage")
elif 21<age<40:
    print("adulthood")
elif age>45:
    print("senior citizen")
else:
    print("newborn")


#Print "Pass" if marks >= 40 using shorthand.
marks=int(input("enter the marks"))
print("pass") if marks>=45 else print("fail")

#using pass keyword

#Write a program where: If number > 0 → do nothing (use pass) Else → print "Negative"
number=int(input("enter the number"))
if number>0:
    pass
else:
   

#Check if a number is:Positive even Positive odd Negtive Zero
 num1=int(input("enter the num"))
if num1>0 and num1%2==0:
    print("positive ,even")
elif num1>0 and num1%2!=0:
    print("positive,odd")
elif num1<0 and num1%2==0:
    print("negative,even")
elif num1<0 and num1%2!=0:
    print("negative,odd")
else:
    print("zero")


#Take three numbers and print the largest.
num1, num2, num3 = map(int, input("enter 3 numbers: ").split())

if num1 > num2 and num1 > num3:
    print("num1 is greatest")
elif num2 > num3:
    print("num2 is greatest")
else:
    print("num3 is greatest")


#Electricity bill:
"""
Units <= 100 → ₹2/unit

101-200 → ₹5/unit

Above 200 → ₹8/unit 
"""
units=int(input("enter the units"))
if units<=100:
    print("bill is :",units*2,"rupees")
elif 101<units<200:
    print("the bill is :",units-100*5+ 100*2)
elif units>200:
    print("the bill is :",units-200*8+ 100*2 + 100*5 )
else:
 print("negative")