"""
LESSON 8: Lists & List Comprehension

1. List Basics
2. Sorting & Reversing
3. List Comprehension
4. append() vs extend()
5. Practice
"""

print("=" * 60)
print("LESSON 8: LISTS")
print("=" * 60)

# ==========================================================
# 1. LIST BASICS
# ==========================================================

print("\n1. LIST BASICS")

fruits = ["apple", "banana", "cherry"]

print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("orange")
print(f"append(): {fruits}")

fruits.remove("banana")
print(f"remove(): {fruits}")

item = fruits.pop()
print(f"pop(): {item}")
print(fruits)

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
print(numbers[2:])
print(numbers[1:4])

# ==========================================================
# 2. SORTED & REVERSED
# ==========================================================

print("\n2. SORTED & REVERSED")

numbers = [3, 1, 4, 5, 2]

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(list(reversed(numbers)))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# ==========================================================
# 3. LIST COMPREHENSION
# ==========================================================

print("\n3. LIST COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]
print(squares)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

words = ["hello", "world", "python"]

upper = [w.upper() for w in words]
print(upper)

# ==========================================================
# 4. append() vs extend()
# ==========================================================

print("\n4. APPEND vs EXTEND")

a = [1, 2]
a.append([3, 4])
print(a)

b = [1, 2]
b.extend([3, 4])
print(b)

# ==========================================================
# 5. PRACTICE
# ==========================================================

print("\n5. PRACTICE")

students = ["Alice", "Bob", "Charlie"]

students.append("David")
students.remove("Bob")

print(students)

scores = [85, 92, 78, 95]

print(sorted(scores))
print(sorted(scores, reverse=True))

prices = [29.99, 15.50, 42.00]

rounded = [round(p) for p in prices]
print(rounded)

expensive = [p for p in prices if p > 30]
print(expensive)
