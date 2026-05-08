#creating sets
set1={"raj","neeli",23,True,1,0,"raj","mango",34.2}
print(set1)
print(len(set1))
print(type(set1))


#accessing elements
nums={22,32,12,33,44,23,11,222,333,3}
for x in nums:
    print(x)
print(list(nums))
nums = {5, 15, 25}
print("Elements:", list(nums))
print(100 in nums)

#adding elements
empty=set({})
empty.add("mango")
print(empty)
empty.update(("kiwi","watermelon"))
print(empty)

#remove elements
nums={22,32,12,33,44,23,11,222,333,3}
nums.remove(32)
nums.discard(44)
print(nums)

#union,intersection,difference on sets
set1={"red","purpull","green","black","pink"}
set2={"white","gold","blue","pink"}
set3=set1.union(set2)
set3=set1|set2
set4=set1&set2
set5=set1-set2
set6=set1>=set2
set7=set1<=set2
print(set3)
print(set4)
print(set5)
print(set6)
print(set7)

#conerting list/tuples into sets
tuple1=("red","blue","green","black","pink","white")
set111=set(tuple1)
print(set111)

#set relationships
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint({4, 5}))

#frozen sets
fs = frozenset([1, 2, 3])
print(fs)
