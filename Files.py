#Reading a File
file = open("data.txt", "r")
print(file.read())
file.close()

#Writing a file
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

#Appending to file
file = open("data.txt", "a")
file.write("\nWelcome to Python")
file.close()

#with open()
with open("data.txt", "r") as file:
    print(file.read())


#json.dumps()
import json
student = {
    "name": "Aman",
    "age": 20
}
result = json.dumps(student)
print(result)

#json.loads()
import json
data = '{"name": "Aman", "age": 20}'
result = json.loads(data)
print(result)
print(result["name"])

#json.dump()
import json
student = {
    "name": "Aman",
    "age": 20
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


#json.load()
import json
with open("student.json", "r") as file:
    data = json.load(file)
print(data)