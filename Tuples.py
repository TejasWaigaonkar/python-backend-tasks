
#Create a tuple
numbers = (10, 20, 30, 40, 50)
print("Original Tuple:", numbers)

#Access elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

#Slicing
print("Slicing:", numbers[1:4])

#Concatenation
new_tuple = (60, 70)
result = numbers + new_tuple
print("Concatenation:", result)

#Repetition
print("Repetition:", numbers * 2)

#Length
print("Length:", len(numbers))

#Count occurrences of 20
print("Count of 20:", numbers.count(20))

#Find index of 30
print("Index of 30:", numbers.index(30))

#Find index of 20
print("Index of 20:", numbers.index(20))

#Check if 40 exists
print("40 exists:", 40 in numbers)

#Find length
print("Length:", len(numbers))