#for loop inside a function
def mul(a):
    print(3 * a)

for i in [4, 6]:
    mul(i)

#Write a function that returns the sum of two numbers.
def sum(a,b):
    return a+b
print(sum(4,5))

#Write a function that returns the square of a number.
def square(a):
    return a**2
print(square(4))

#Write a function that returns True if a number is positive, else False.
def posorneg(n):
    return "true" if n>0 else "false"
print(posorneg(9))


#Write a function that returns None explicitly.
def my_func(a,b):
    print(a+b)
   
a=my_func(3,4)
print(a)


#Write a function that takes two arguments and returns their product.
def add(a,b):
    return a*b
print(add(3,4))

#Write a function that accepts string and integer and prints both.
def my_func():
    a=str(input("enter a value:"))
    b=int(input("enter b value:"))
    print(a,b)
my_func()


#Write a function that takes a list and prints its length.
def my_func():
    lst=input("enter the elements with comma").split(",")
    print(len(lst))
my_func()

#Write a function that takes a list and prints its length.
def my_func(a):
    print(len(a))

my_func([10, 20, 30, 40])


#Write a function with a default parameter value.
def my_func(country="india"):
    print(country)
my_func("norway")
my_func()
my_func("paris")
my_func("newzeland")


#Call the function with and without passing the argument.
#without passing the arguments
def fruits():
    fruit=input("enter  the fruits:").split(",")
    print(fruit)
fruits() 

#with passing the arguments
def my_func(fruits):
    for i in fruits:
        print(i)
a=["mango","watermelon","orange"]
my_func(a)
    
#Write a function that calculates simple interest using default rate.
def interest(rate=40):
    interest_money=23*rate*23/100
    print(interest_money)
interest()

#What happens if default arguments are written before non-default? Try it
def func(a,b,m,d=10):
    x=a+b+m+d
    print(x)
func(12,33,22)

#Call a function with fewer positional arguments than required.
def my_func(name,age,height):
    print("my name is:",name)
    print("my age is :",age)
    print("my height is:",height)
my_func("nayana",23,5.4)

#Change the order of arguments while calling and observe output.
def my_func(name,age,height):
    print("my name is:",name)
    print("my age is :",age)
    print("my height is:",height)
my_func(23,"nayana",5.5)

#Write a function and call it using keyword arguments.
def details(name="nayana",age=23,dob="may 1st"):
    print("the name is :",name)
    print(age)
    print(dob)
details(name="siri", age=30, dob="Jan 10th")


#Write a function that uses only keyword arguments.
def func(*,a,b,c,d):
    s=a+b+c+d
    print(s)
func(a=3,b=4,c=2,d=3)

#Call the same function using positional + keyword arguments.
def func(c,d,/,*,a,b):
    s=a+b+c+d
    print(s)
func(2,7,a=3,b=4,)

#Call a function using keyword arguments in different order.
def math(a,b,/,*,c,d):
    sum=a+b+c+d
    print(sum)
math(2,3,c=7,d=6)

#Try passing keyword-only arguments as positional.
def fruits(*,a,b,c):
    print(f"a={a},b={b},c={c}")
fruits("apple","banana",a="mango")

#Write a function that accepts any number of arguments and prints them.
def fruits(*fruit):
    print(fruit[0])
    print(fruit[2])
fruits("mango","apple","banana","watermelon")

#Write a function that finds the sum of numbers using *args.
def num(*summ):
    total=0
    for i in summ:
      total+=i
    return total
a=num(2,3,4,5,6)
print(f"The total sum is: {a}")


