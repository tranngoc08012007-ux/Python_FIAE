Lesson 8: List & List Comprehension — Exercises

Exercise 1: List Basics

Problem:

Write a program that:

1. Creates a list students = ["Alice", "Bob", "Charlie", "Diana"]
2. Appends "Eve" to the end.
3. Removes "Bob" from the list.
4. Prints "Charlie" using negative indexing.
5. Prints the first 2 students using slicing.

⸻

Exercise 2: Sorted & Reversed

Problem:

Write a program that:

1. Creates a list scores = [85, 92, 78, 95, 88].
2. Prints the list sorted from high to low without modifying the original.
3. Prints the reversed list without modifying the original.
4. Prints the original list.
5. Sorts the original list using .sort() and prints it.

⸻

Exercise 3: List Comprehension

Problem:

Given:

prices = [29.99, 15.50, 42.00, 8.75, 99.99, 33.25]

Use list comprehension to:

1. Create a new list of rounded prices.
2. Keep only prices greater than 30.
3. Create a list of formatted strings:

Price: 29.99€

⸻

Exercise 4: extend() vs append()

Problem:

Write a program that:

1. Creates a list:

cart = ["apple", "banana"]

2. Uses .extend() to add:

["orange", "mango", "grape"]

3. Prints the result.
4. Creates another list and uses .append() with the same list, then prints the result to demonstrate the difference.

⸻

Challenge 1

Given:

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 30},
    {"name": "Monitor", "price": 400},
    {"name": "Keyboard", "price": 80}
]

Use list comprehension to:

1. Extract product names.
2. Keep only products with price > 50.
3. Format each as:

Product: Name (Price: $X)

⸻

Challenge 2

Given:

scores = [45, 67, 78, 92, 88, 56, 95, 72, 61, 89, 73, 84]

Write a program to:

1. Filter passing scores (>= 70).
2. Sort them from high to low.
3. Get the top 3 scores.
4. Format each as:

Score 1: 95/100

⸻

Challenge 3

Given:

words = ["python", "java", "javascript", "c++", "go"]

Use list comprehension to:

1. Convert all words to uppercase.
2. Keep only words with length greater than 4.
3. Add the prefix "Language: " to each word.
