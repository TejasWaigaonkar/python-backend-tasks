# def Student():
#     yield "College name"
#     yield "Canteen"
#     yield "Ground"

# s1 = Student()
# for c1 in s1:
#     print(c1)
#-----------------------------

# #next()
# def numbers():
#     yield 10
#     yield 20
#     yield 30

# n = numbers()
# print(next(n))
# print(next(n))
# print(next(n))
#----------------------------------

# #infinite generators
# def infinite_drinks():
#     count = 1
#     while True:
#         yield f"Refill {count}"
#         count += 1

# refill = infinite_drinks()

# for d1 in range(5):
#     print(next(refill))
#-----------------------------------

def customer():
    print("Welcome to the store!")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield
stall = customer()
next(stall) #starts the generator
stall.send("Pizza")
stall.send("Burger")
#----------------------------------

def local_foods():
    yield "Maggi"
    yield "Dosa"
def imported_foods():
    yield "Burger"
    yield "Pizza"
def full_name():
    yield from local_foods()
    yield from imported_foods()
for food in full_name():
    print(food)
#------------------------------------

def food_stall():
    try:
        while True:
            order = yield "Waiting for the order"
    except:
        print("Stall closed")

stall = food_stall()
print(next(stall))
stall.close()
#-------------------------------------