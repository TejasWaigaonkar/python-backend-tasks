#if
age = 20
if age >= 18:
    print("Eligible to vote")

#if-else
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

#if-elif-else
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

#nested if-else
income = 12000
if age >= 21:
    if income >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible: Income too low")
else:
    print("Not eligible: Age must be 21 or above")

#ternary operator
order_amount = int(input("Enter order amount: "))
delivery_fees = 0 if order_amount >= 300 else 10
print(f"Delivery fees: {delivery_fees}")

#match case
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")