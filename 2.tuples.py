#print the tuple
languages=("kannada","english","python","maths","c++")
print(languages)
all=("nayana",33,int,34,True,0)
print(all)


#access the tuple
numbers = (10, 20, 30, 40, 50)
print(numbers[0],numbers[2+1+1],numbers[len(numbers)//2])
fruits = ("apple", "banana", "cherry", "date", "fig")
for i in range(4):
   print(fruits)


#updating tuple,convert the list
colors=("red","blue","green","purpule","black","white")
new=list(colors)
new[1] = "pink"
colors =  tuple(new)
print(colors)


#tuple looping
num=(10,20,30,40,50,60,70)
print(num.count(10))
print(num)
for x in num:
    print(x)


print()
i=0
for x in num:
    if x>50:
     print(x)
    i=i+1

#joining tuples
tuple1=(20,30,44,50,67,56)
tuple2=(12,44,55,23,43,22,12,34)
tuple3=tuple1+(tuple2)
print(tuple3)

#finding the count
values = (1, 7, 3, 2, 4,2,2, 2, 5)
print(values.count(2))
print(values.index(7))

