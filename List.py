#accesing the list
nums=[1,2,3,4,5]
print(nums[0])
print(nums[2])
print(nums[2:])

#changing the items
fruits=["mango","banana","pineapple","kiwi","cherry"]
fruits.insert(2,"watermelon")
fruits[3:5]=("melon","kiwi")
print(fruits)


#adding or extending the list
colors=["red","blue"]
colors.append("brown")
colors[2]="white"
colors.insert(1,"yellow")
color2=["black","pink"]
colors.extend(color2)
print(colors)
print(color2)


#removing the items in the list
animals = ["dog", "cat", "lion", "tiger", "elephant"]
animals.remove("lion")
animals.pop(3)
del animals[1]
print(animals)


#list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new2= [x for x in range(5) if x>3]
print(new2) 


#sorting the list
marks = [45, 67, 23, 89, 12, 90]
marks.sort(reverse=True)
print(marks)
marks.sort()
print(marks)


#coping the list
original = [1, 2, 3, 4]
newone=[]
newone=original.copy()
print(newone)
print(original)


#joining the list
list1 = ["a", "b", "c"] 
list2 = [1, 2, 3]
list1+=list2
print(list1)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = [n if n % 2 == 0 else "odd" for n in numbers]
print(new_list)


#zipping the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
paired = list(zip(list1, list2))
print(paired)


#reversing
nums = [1, 2, 3]
print(nums[::-1])   # [3, 2, 1]

