# Lesson 07: Strings

## Practice Exercises

### Topics
- f-strings
- String slicing
- String methods
- String comparison

**Author:** Tran Ngoc

---

## Exercise 1: f-strings

Declare 3 variables:

- `product` (product name)
- `price` (float)
- `quantity` (int)

Use an **f-string** to print a sentence such as:

```
You bought 3 x Laptop for a total of: 1500.00 EUR
```

Requirements:

- Calculate the total directly inside `{}`.
- Do **not** create a separate `total` variable.
- Format the total with **2 decimal places**.

---

## Exercise 2: Slicing

Given:

```python
code = "PY-2026-FIAE-0012"
```

Using **slicing only** (no `split()`), extract:

1. The language code (`"PY"`)
2. The year (`"2026"`)
3. The last 4 characters
4. The entire string reversed

---

## Exercise 3: String Methods

Given:

```python
raw = "   Rohde   &   SCHWARZ   "
```

Write code that:

1. Removes the extra whitespace using `strip()`
2. Converts the whole string to lowercase using `lower()`
3. Replaces `"&"` with `"and"` using `replace()`
4. Splits the result into a list of words using `split()`
5. Prints the resulting list

---

## Exercise 4: String Comparison

Simulate comparing two usernames (no `input()`):

```python
username_input = "Ngoc"
username_stored = "ngoc"
```

Print the result of:

1. A direct comparison using `==`
2. A comparison after converting both strings to lowercase

---

## Exercise 5: Combined Practice (Advanced)

Given:

```python
log_line = "  2026-08-12 | ERROR | Connection Failed  "
```

Write code that:

1. Removes the extra whitespace.
2. Splits the string into **3 parts** using `"|"`.
3. Removes whitespace around each part.
4. Prints the result in the following format:

```text
[ERROR] 2026-08-12: Connection Failed
```
