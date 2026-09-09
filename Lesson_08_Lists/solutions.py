"""
LESSON 8: LIST & LIST COMPREHENSION — SOLUTIONS
"""
# ==================================================
# Exercise 1
# ==================================================
students = ["Alice", "Bob", "Charlie", "Diana"]
students.append("Eve")
students.remove("Bob")
print(students[-2])
print(students[:2])
# ==================================================
# Exercise 2
# ==================================================
scores = [85, 92, 78, 95, 88]
print(sorted(scores, reverse=True))
print(list(reversed(scores)))
print(scores)
scores.sort()
print(scores)
# ==================================================
# Exercise 3
# ==================================================
prices = [29.99, 15.50, 42.00, 8.75, 99.99, 33.25]
rounded_prices = [round(price) for price in prices]
prices_above_30 = [price for price in prices if price > 30]
formatted_prices = [f"Price: {price}€" for price in prices]
print(rounded_prices)
print(prices_above_30)
for item in formatted_prices:
    print(item)
# ==================================================
# Exercise 4
# ==================================================
cart = ["apple", "banana"]
cart.extend(["orange", "mango", "grape"])
print(cart)
cart = ["apple", "banana"]
cart.append(["orange", "mango", "grape"])
print(cart)
# ==================================================
# Challenge 1
# ==================================================
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 30},
    {"name": "Monitor", "price": 400},
    {"name": "Keyboard", "price": 80},
]
product_names = [p["name"] for p in products]
expensive_products = [p for p in products if p["price"] > 50]
formatted_products = [
    f"Product: {p['name']} (Price: ${p['price']})"
    for p in products
]
print(product_names)
print(expensive_products)
for item in formatted_products:
    print(item)
# ==================================================
# Challenge 2
# ==================================================
scores = [45, 67, 78, 92, 88, 56, 95, 72, 61, 89, 73, 84]
passing_scores = [score for score in scores if score >= 70]
passing_scores = sorted(passing_scores, reverse=True)
top_3 = passing_scores[:3]
formatted_scores = [
    f"Score {i + 1}: {score}/100"
    for i, score in enumerate(top_3)
]
for item in formatted_scores:
    print(item)
# ==================================================
# Challenge 3
# ==================================================
words = ["python", "java", "javascript", "c++", "go"]
uppercase_words = [word.upper() for word in words]
long_words = [word for word in words if len(word) > 4]
prefixed_words = [f"Language: {word}" for word in words]
print(uppercase_words)
print(long_words)
for item in prefixed_words:
    print(item)
