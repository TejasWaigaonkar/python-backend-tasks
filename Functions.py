#function
def order_name(name):
    print(f"{name}")
order_name("Pizza")
#---------------------------

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_orders():
    print("Filtering the sales data")

def summarize_data():
    print("Summarizing the sales data")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()

generate_report()
#------------------------------------

#Local Scope
def greet():
    name = "Aman"
    print(name)
greet()
#---------------------------------

#Enclosed Scope
def outer():
    x = 20
    def inner():
        print(x)
    inner()
outer()
#---------------------------------

#Non-Local Scope
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()

#Global Scope
x = 10
def show():
    global x
    x = 20
    print("Inside:", x)
show()
print("Outside:", x)

#args , kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)
special_chai("Cinnamon", "Cardomon", sweetner="Honey", foam="yes")
#----------------------------------------------------------------=

#lambda
square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))
#-------------------------------------------------------------