"""
LESSON 8: Lists & List Comprehension
======================================
This file covers:
- Part 1: List Basics (initialization, append, remove, pop, slicing)
- Part 2: Sorted & Reversed
- Part 3: List Comprehension
- Bonus: extend() vs append()

Target: Fachinformatiker Anwendungsentwicklung (FIAE)
Environment: Python 3.11, VS Code, venv, Windows
"""

print("=" * 70)
print("LESSON 8: LISTS & LIST COMPREHENSION")
print("=" * 70)


# ============================================================================
# PART 1: LIST BASICS
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: LIST BASICS - Initialization, append, remove, pop, slicing")
print("=" * 70)

# Initialize a list
fruits = ["apple", "banana", "cherry"]
print(f"\n1. Initialize list: {fruits}")

# Access elements by index (0-based)
print(f"2. Access index 0: {fruits[0]}")
print(f"3. Access index -1 (last element): {fruits[-1]}")

# Append: add element to the end
fruits.append("orange")
print(f"4. After append('orange'): {fruits}")

# Remove: delete by value
fruits.remove("banana")
print(f"5. After remove('banana'): {fruits}")

# Pop: remove by index, return the value
removed_fruit = fruits.pop(0)  # Remove first element
print(f"6. Popped element: {removed_fruit}")
print(f"   Remaining list: {fruits}")

# Slicing: extract a portion of the list
numbers = [10, 20, 30, 40, 50]
print(f"\n7. Original list: {numbers}")
print(f"   Slice [0:3]: {numbers[0:3]}")      # From index 0 to 2
print(f"   Slice [1:]: {numbers[1:]}")        # From index 1 to end
print(f"   Slice [:3]: {numbers[:3]}")        # From start to index 2


# ============================================================================
# EXERCISE 1: LIST BASICS
# ============================================================================
print("\n" + "-" * 70)
print("EXERCISE 1: List Basics")
print("-" * 70)

students = ["Alice", "Bob", "Charlie", "Diana"]

students.append("Eve")
students.remove("Bob")

print(f"Students list after append/remove: {students}")
print(f"Index of Diana (using -2): {students[-2]}")
print(f"First 2 students (slice [:2]): {students[:2]}")


# ============================================================================
# PART 2: SORTED & REVERSED
# ============================================================================
print("\n" + "=" * 70)
print("PART 2: SORTED & REVERSED")
print("=" * 70)

numbers = [3, 1, 4, 1, 5, 9, 2]
words = ["zebra", "apple", "mango", "banana"]

print(f"\nOriginal list: {numbers}")

# sorted(): returns new sorted list, doesn't modify original
sorted_asc = sorted(numbers)
print(f"sorted() ascending: {sorted_asc}")
print(f"Original still unchanged: {numbers}")

# sorted() with reverse parameter
sorted_desc = sorted(numbers, reverse=True)
print(f"sorted(reverse=True) descending: {sorted_desc}")

# Sorted with strings
print(f"\nOriginal words: {words}")
sorted_words = sorted(words)
print(f"Sorted words: {sorted_words}")

# reversed(): returns iterator, convert to list
reversed_list = list(reversed(numbers))
print(f"\nReversed list: {reversed_list}")
print(f"Original still unchanged: {numbers}")

# .sort() and .reverse(): modify original list IN-PLACE
print("\n--- Using .sort() and .reverse() (modify original) ---")

numbers_copy = numbers.copy()  # Make a copy to avoid changing original

numbers_copy.sort()
print(f"After .sort(): {numbers_copy}")

numbers_copy.reverse()
print(f"After .reverse(): {numbers_copy}")


# ============================================================================
# EXERCISE 2: SORTED & REVERSED
# ============================================================================
print("\n" + "-" * 70)
print("EXERCISE 2: Sorted & Reversed")
print("-" * 70)

scores = [85, 92, 78, 95, 88]

print(f"Original scores: {scores}")

# Sort from high to low
sorted_high_to_low = sorted(scores, reverse=True)
print(f"Sorted (high to low): {sorted_high_to_low}")

# Reversed
reversed_scores = list(reversed(scores))
print(f"Reversed: {reversed_scores}")

# Original unchanged
print(f"Original still unchanged: {scores}")

# Modify original
scores.sort()
print(f"After .sort() (original modified): {scores}")


# ============================================================================
# PART 3: LIST COMPREHENSION
# ============================================================================
print("\n" + "=" * 70)
print("PART 3: LIST COMPREHENSION")
print("=" * 70)

# Basic: Apply operation to each element
print("\n--- Basic: Apply operation ---")

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Old way (traditional for loop)
squared_old = []

for num in numbers:
    squared_old.append(num ** 2)

print(f"Old way (for loop): {squared_old}")

# New way (list comprehension)
squared_new = [num ** 2 for num in numbers]
print(f"List comprehension: {squared_new}")


# Filter: Keep only elements that match condition
print("\n--- Filter: Keep only even numbers ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]

print(f"Original: {numbers}")
print(f"Even numbers: {even_numbers}")

# Filter AND transform: Odd numbers squared
odd_squared = [num ** 2 for num in numbers if num % 2 != 0]
print(f"Odd numbers squared: {odd_squared}")


# String operations
print("\n--- String operations with list comprehension ---")

words = ["hello", "world", "python"]
print(f"Original: {words}")

# Convert to uppercase
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

# Keep only words longer than 5 characters
long_words = [word for word in words if len(word) > 5]
print(f"Words with length > 5: {long_words}")


# ============================================================================
# EXERCISE 3: LIST COMPREHENSION
# ============================================================================
print("\n" + "-" * 70)
print("EXERCISE 3: List Comprehension")
print("-" * 70)

prices = [29.99, 15.50, 42.00, 8.75, 99.99, 33.25]

print(f"Original prices: {prices}")

# 1. Round all prices
rounded_prices = [round(p) for p in prices]
print(f"Rounded prices: {rounded_prices}")

# 2. Keep only prices > 30
prices_above_30 = [p for p in prices if p > 30]
print(f"Prices > 30: {prices_above_30}")

# 3. Format as strings
formatted_prices = [f"Price: {p:.2f}€" for p in prices]

print("Formatted prices:")

for formatted in formatted_prices:
    print(f"  {formatted}")


# ============================================================================
# BONUS: EXTEND vs APPEND
# ============================================================================
print("\n" + "=" * 70)
print("BONUS: EXTEND() vs APPEND()")
print("=" * 70)

print("\n--- append(): adds entire object as single element ---")

list1 = [1, 2, 3]
print(f"Before: {list1}")

list1.append([4, 5, 6])

print(f"After .append([4, 5, 6]): {list1}")
print(f"Result: NESTED LIST (list inside list) ❌")


print("\n--- extend(): adds each element individually ---")

list2 = [1, 2, 3]
print(f"Before: {list2}")

list2.extend([4, 5, 6])

print(f"After .extend([4, 5, 6]): {list2}")
print(f"Result: FLAT LIST ✓")


print("\n--- extend() with string (strings are iterable) ---")

list3 = ["a", "b"]

list3.extend("XY")

print(f"extend('XY'): {list3}")


print("\n--- extend() with tuple ---")

list4 = [10, 20]

list4.extend((30, 40, 50))

print(f"extend((30, 40, 50)): {list4}")


# ============================================================================
# EXERCISE 4: EXTEND vs APPEND
# ============================================================================
print("\n" + "-" * 70)
print("EXERCISE 4: Extend vs Append")
print("-" * 70)

cart = ["apple", "banana"]
print(f"Initial cart: {cart}")

# Using extend()
cart.extend(["orange", "mango", "grape"])
print(f"After .extend(['orange', 'mango', 'grape']): {cart}")

# Comparison with append()
cart_append = ["apple", "banana"]

cart_append.append(["orange", "mango", "grape"])

print(f"Using .append() instead: {cart_append}")
print("Notice: .append() creates a nested list!")


# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("LESSON 8 SUMMARY")
print("=" * 70)
