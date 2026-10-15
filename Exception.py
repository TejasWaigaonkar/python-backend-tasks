#try, except, else and finally
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")
#-----------------------------------------------------

#multiple exception
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
# process_order("masala", two)
#---------------------------------------------------------

