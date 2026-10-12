
#Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "branch": "Computer Science"
}
print("Original Dictionary:", student)

#Access elements
print("Name:", student["name"])
print("Age:", student.get("age"))

#Add a new element
student["city"] = "Pune"
print("After Adding:", student)

#Update an element
student["age"] = 21
print("After Updating:", student)

#Remove an element
student.pop("branch")
print("After Removing:", student)

#Print all keys
print("Keys:", student.keys())

#Print all values
print("Values:", student.values())

#Print key-value pairs
print("Items:", student.items())

#Remove last inserted item
student.popitem()
print("After popitem:", student)

#Add multiple elements
student.update({
    "branch": "Computer Science",
    "marks": 85
})
print("After Update:", student)

#Modify an existing value
student.update({"age": 21})
print("After Changing Age:", student)

#Delete an element
del student["branch"]
print("After Delete:", student)

#Copy dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

#Check if a key exists
print("Name exists:", "name" in student)

#Clear the copied dictionary
new_student.clear()
print("After Clear:", new_student)

#Original dictionary remains unchanged
print("Original Dictionary:", student)


#nested dictionary
#Create a nested dictionary
students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Amit",
        "age": 21,
        "marks": 90
    }
}
print("Original Dictionary:", students)

#Access student details
print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Marks:", students["student2"]["marks"])

#Add a new student
students["student3"] = {
    "name": "Priya",
    "age": 19,
    "marks": 95
}
print("After Adding:", students)

#Update marks
students["student1"]["marks"] = 88
print("Updated Marks:", students["student1"])

#Delete a student
del students["student2"]
print("After Deleting:", students)

#Display all students using a loop
for key, value in students.items():
    print(key, ":", value)
