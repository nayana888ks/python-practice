#dictionary
student={
    "name":"shiva",
    "usn":"4vm23cs003",
    "branch":"cse",
    "college":"vviet"
}
print(student)
print(len(student))
print(type(student))

#accessing dict
student={
    "name":"shiva",
    "usn":"4vm23cs003",
    "branch":"cse",
    "college":"vviet"
}
print(student["usn"])
print(student.get("branch"))

#changing the items
student={
    "name":"shiva",
    "usn":"4vm23cs003",
    "branch":"cse",
    "college":"vviet"
}
student["college"]="atme"
student.update({"usn":"4vm23cs002"})
print(student)

#adding items
car={}
car["brand"]="ferrari"
print(car)
car.update({"color":"red","num":333333})
print(car)

#removing items
student2={
    "name":"shivani",
    "usn":"4vm23cs022",
    "branch":"ec",
    "college":"vviet"
}
student2.pop("usn")
student2.popitem()
print(student2)
student2.clear()
print(student2)

#looping
student3={
    "name":"shivani",
    "usn":"4vm23cs022",
    "branch":"ec",
    "college":"vviet"
}
for x in student3.keys():
    print(x)
    
for x in student3.values():
    print(x)

for x,y in student3.items():
    print(x,y)


#coping a dict
student3={
    "name":"shivani",
    "usn":"4vm23cs022",
    "branch":"ec",
    "college":"vviet"
}
student9={}
student9=student3.copy()
print(student9)

#nested dictionary
family={
    "family1":{
        "father":"ravi",
        "mother":"sihi",
        "son":"arman"

    },
    "family2":{

        "father":"sushanth",
        "mother":"shivani",
        "son":"vivek"
    }
}
print(family)