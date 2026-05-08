#Write a program using a while loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1


#Write a program using a while loop to print the multiplication table of a given number.
num=int(input("enter the number"))
i=1
while i<=10:
    print(num,"X", i ,"=" ,num * 1 )
    i+=1


#Write a program to keep asking the user for input until they enter 0, then stop.
while True:
    data=int(input("enter the number"))
    if data==0:
        break
print("loop over")


#Count number of digits using
num = int(input("Enter a number: "))
count =0 
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)


#Reverse a number using while
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)


#write a program to calculate the sum of digits of a given number using a while loop.
numbers=int(input("enter the number"))
sum=0
while numbers>0:
    digit=numbers % 10
    sum+=digit
    numbers=numbers//10
print("sum of the digits",sum)


#Check Palindrome Number using while
num=int(input("enter the number"))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num //= 10
if original==rev:
    print("its a palindrome")
else:
    print("it's not")



"""Find Smallest Digit in a Number
Clue:
Take last digit using % 10
Assume smallest digit is 9 at start
Compare each digit with smallest
Update smallest if digit is smaller
Remove digit using // 10"""

num=int(input("enter the num"))
smallest=9
while num>0:
    digit=num%10
    if smallest>digit:
        print("smallest",digit)
    num=num//10


"""Count How Many Times a Digit Appears
Clue:
Take input number
Take input digit
Extract digits one by one using % 10
If extracted digit == given digit → increase counter
Remove digit using // 10"""

num=int(input("enter the number"))
digit=int(input("enter the digit"))
count=0
while num>0:
    digit1=num%10
    if digit==digit1:
        count+=1
    num=num//10
print("Digit appears", count, "times")



"""Power of a Number using while
Clue:
Initialize result = 1
Multiply result by base
Reduce exponent by 1 each loop
stop when exponent becomes 0"""

base=int(input("enter the base"))
exponent=int(input("enter the exponent"))
result=1
while exponent>0:
    result=result*base
    exponent-=1
print("the final value is :",result)


#reversing number in descending order
x = int(input("enter"))
while x>=0:
   print(x,end=" ")
   x-=1
