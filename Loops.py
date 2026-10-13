#for
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")
#-----------------------------

menu = ["Pizza", "Burger", "Pasta", "Salad"]
for idx, item in enumerate(menu, start=1):
    print(f"{idx}: {item}")
#------------------------------

names = ["Alice", "Bob", "Charlie"]
bills = [255, 300, 150]
for name, bill in zip(names, bills):
    print(f"{name} paid{bill} rupees")




#while
i = 1
while i <= 10:
    print(f"2 x {i} = {2 * i}")
    i += 1
#-----------------------------------------

temperature = 40
while temperature < 100:
    print(f"Current temperature: {temperature}°C")
    temperature += 15
#-----------------------------------------


#break
for i in range(1, 6):
    if i == 3:
        break
    print(i)


#continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


#prime
#for
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")


#while
num = int(input("Enter a number: "))
i = 2
is_prime = True

if num <= 1:
    is_prime = False

while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")