essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices #union
print(f"All_spices: {all_spices}")

common_spices = essential_spices & optional_spices #intersection
print(f"Common_spices: {common_spices}")

only_essential_spices = essential_spices - optional_spices #difference
print(f"Only_essential_spices: {only_essential_spices}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

#Task
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(branch_a_products)
print(branch_b_products)

print(branch_a_products.union(branch_b_products))

print(branch_a_products.intersection(branch_b_products))

print(branch_a_products.difference(branch_b_products))

print("ketchup" in branch_a_products)

essential_items = frozenset(["milk", "bread", "ketchup"])
print(essential_items)

#Sets Comprehensions
numbers = {i for i in range(1, 6)}
print(numbers)
#--------------------
even = {i for i in range(1, 11) if i % 2 == 0}
print(even)

#Dictionary Comprehensions