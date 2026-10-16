# class Chai:
#     origin = "India"  #class attribute
# print(Chai.origin)

# Chai.is_hot = True
# print(Chai.is_hot)

# masala = Chai()
# print(masala.origin)
#----------------------------------------

# #attribute shadowing
# class Chai:
#     temperature = "hot"
#     strength = "strong"

# cutting = Chai()
# print(cutting.temperature)

# cutting.temperature = "Mild"
# print(cutting.temperature)
# print(Chai.temperature)

# del cutting.temperature
# print(cutting.temperature)
#-----------------------------------------

# #self argument
# class Chaicup:
#     size = 150

#     def describe(self):
#         return f"A {self.size}ml of chai cup"

# cup = Chaicup()
# print(cup.describe())
#----------------------------------------

# #__init__
# class ChaiOrder:
#     pass

#     def __init__(self, type_, size):  #i took type_ cause its a operator, a fn which gives what we ask for
#         self.type = type_
#         self.size = size

#     def summary(self):
#         return f"{self.size}ml of {self.type} chai"

# order = ChaiOrder("Masala", 200)
# print(order.summary())
#---------------------------------------------

# class Student():
#     pass

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f"{self.name} is {self.age} years old"

# s1 = Student("Tejas", 20)
# print(s1.display())
#-----------------------------------------------

class SmartDevice:
    brand = "HomeTech"   #class attribute
    
    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status
        self.brand = "CustomBrand"    #instance attribute
        
    def get_status(self):
        if self.power_status:
            return self.device_name + " is ON - " + self.brand
        else:
            return self.device_name + " is OFF - " + self.brand
            
d1 = SmartDevice("AC", True)
d2 = SmartDevice("Fan", False)

print(d1.get_status())
print(d2.get_status())