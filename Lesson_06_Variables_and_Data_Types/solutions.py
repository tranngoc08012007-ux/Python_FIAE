"""
Lesson 06: Variables & Data Types - Solutions
See exercises.md for the problem statements.
"""

# ============================================================
# EXERCISE 1: Personal Information
# ============================================================

name = "Ngoc"          # str
age = 18                # int
height = 1.75            # float
graduated = False        # bool
note = None              # NoneType

print("Data type of each variable:")
print(type(name))
print(type(age))
print(type(height))
print(type(graduated))
print(type(note))

print("-" * 40)

print(f"Name: {name} | Age: {age} | Height: {height}m | Graduated: {graduated} | Note: {note}")


# ============================================================
# EXERCISE 2: Simple Calculator
# ============================================================

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(
    f"{num1} + {num2} = {num1 + num2}",
    f"{num1} - {num2} = {num1 - num2}",
    f"{num1} * {num2} = {num1 * num2}",
    f"{num1} / {num2} = {num1 / num2}",
    f"Floor: {int(num1) // int(num2)}",
    f"Remainder: {int(num1) % int(num2)}",
    sep=" | "
)


# ============================================================
# EXERCISE 3: Purchase Invoice
# ============================================================

product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

subtotal = unit_price * quantity
tax = subtotal * 0.1
grand_total = subtotal + tax

print("===== INVOICE =====", end="\n")
print(f"Product: {product_name}", end="\n")
print(f"Unit price: {unit_price} VND", end="\n")
print(f"Quantity: {quantity}", end="\n")

print(f"Subtotal: {subtotal} VND", end="\n")
print(f"Tax (10%): {tax} VND", end="\n")
print(f"Grand total: {grand_total} VND", end="\n")
print("====================", end="\n")

print("\nData type of grand_total:", type(grand_total))
print(
    "Explanation: grand_total is a float because it is the result of "
    "adding subtotal (float) and tax (float). In Python, any arithmetic "
    "operation involving at least one float always returns a float."
)