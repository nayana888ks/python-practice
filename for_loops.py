"""You are given a number N, you need to print its multiplication table."""
N=int(input("enter the number"))
for i in range(1,11):
    print(f" {N * i}", end=" ")


#Count Digits in a Number
num=int(input("enter the number"))
count=0
for x in str(num):
   count+=1
print("total number of digits :",count)
   

#sum of digits
num=int(input("enter the number"))
sum = 0
for x in str(num):
   digit=num%10
   sum=digit + sum
print("total sum of digits is :",sum)


#reverse a number
num=int(input("enter the number"))
rev=0
for x in str(num) :
   digit=num%10
   rev=digit
   num-=1
   print(rev,end=" ")
   

"""Armstrong Number Check
First, count how many digits the number has.
For each digit:
Raise it to the power of number of digits.
Add to a sum.
Compare the final sum with the original number.
Key idea: “Each digit contributes something special."""

num=int(input("enter the number"))
digit=len(str(num))
total=0
for x in str(num):
      total=total+ int(x)**digit
print(num)
print(total)

if num==total:
        print("its amstrong")
else:
      print("not amstrong")  



#Factorial Without Built-in Functions
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1 ):
    fact = fact * i

print("Factorial is:", fact)



#Star Pattern Printing (Increasing Triangle)
rows = int(input("enter the rows"))
for i in range(0, rows+1, 1):
    for j in range(i):
        print("*", end="")
    print()


#pyramid logic
rows = int(input("enter the row"))
for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2*i - 1):
        print("*", end="")
    print()




#Count Vowels in a String
text = input("Enter a string: ")
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)



#Print Prime Numbers in a Range (1 to 50)
for num in range(2, 51):     # loop through numbers from 2 to 50
    prime = True             # assume number is prime

    for i in range(2, num):     # check divisibility
        if num % i == 0:        # if divisible
            prime = False    # not a prime
            break          # stop checking further

    if prime:                # if still prime
        print(num)


#Frequency of Each Character
text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


import keyword
print("The list of keywords are : ")
print(keyword.kwlist)