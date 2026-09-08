# BÀI 8: LIST & LIST COMPREHENSION - GIÁO ÁN TIẾNG VIỆT

**Mục tiêu:** Hiểu sâu về List — công cụ cơ bản nhất trong Python và trong lập trình thực tế

---

## 📌 PHẦN 1: LIST CƠ BẢN

### 1.1 List là cái gì?

**List** (danh sách) là một **container** dùng để lưu trữ nhiều giá trị theo thứ tự.

```python
fruits = ["apple", "banana", "cherry"]
```

**Đặc điểm của List:**
- ✅ Lưu được **nhiều giá trị** cùng lúc
- ✅ Có **thứ tự** (phần tử thứ 1, thứ 2, ...)
- ✅ Có thể **thay đổi** (mutable) — thêm/xóa/sửa phần tử
- ✅ Truy cập bằng **chỉ số** (index) bắt đầu từ **0**

---

### 1.2 Tạo List

```python
# Cách 1: Dùng ngoặc vuông [ ]
fruits = ["apple", "banana", "cherry"]

# Cách 2: List rỗng
empty_list = []

# Cách 3: Danh sách số
numbers = [1, 2, 3, 4, 5]

# Cách 4: Danh sách hỗn hợp (không khuyến khích trong thực tế)
mixed = [1, "apple", 3.14, True]
```

---

### 1.3 Truy cập phần tử (Indexing)

```python
fruits = ["apple", "banana", "cherry"]

# Index dương (từ đầu)
print(fruits[0])   # "apple" (phần tử đầu tiên)
print(fruits[1])   # "banana" (phần tử thứ hai)
print(fruits[2])   # "cherry" (phần tử thứ ba)

# Index âm (từ cuối)
print(fruits[-1])  # "cherry" (phần tử cuối cùng)
print(fruits[-2])  # "banana" (phần tử thứ hai từ cuối)
print(fruits[-3])  # "apple" (phần tử thứ ba từ cuối)
```

**⚠️ Lưu ý:** Index bắt đầu từ **0**, không phải 1!

---

### 1.4 Cắt List (Slicing)

```python
numbers = [10, 20, 30, 40, 50]

# Cú pháp: list[start:end]
# ⚠️ Lưu ý: end KHÔNG bao gồm phần tử ở vị trí end

print(numbers[0:3])   # [10, 20, 30]      — từ index 0 đến 2
print(numbers[1:4])   # [20, 30, 40]      — từ index 1 đến 3
print(numbers[2:])    # [30, 40, 50]      — từ index 2 đến cuối
print(numbers[:3])    # [10, 20, 30]      — từ đầu đến index 2
print(numbers[:])     # [10, 20, 30, 40, 50]  — toàn bộ list (copy)
print(numbers[-2:])   # [40, 50]          — 2 phần tử cuối cùng
```

**Mnemonic:** `[start:end]` = "lấy từ start, dừng TRƯỚC end"

---

### 1.5 Thêm phần tử: .append()

```python
fruits = ["apple", "banana"]

# .append(item) — thêm 1 phần tử vào CUỐI list
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Thêm lần nữa
fruits.append("orange")
print(fruits)  # ["apple", "banana", "cherry", "orange"]
```

**Đặc điểm:**
- Thêm vào **cuối** list
- Chỉ thêm **1 phần tử duy nhất**
- Nếu thêm list → sẽ tạo **list lồng nhau** (❌ không muốn)

---

### 1.6 Xóa phần tử: .remove() & .pop()

#### .remove(value) — Xóa theo giá trị

```python
fruits = ["apple", "banana", "cherry"]

# Xóa phần tử có giá trị "banana"
fruits.remove("banana")
print(fruits)  # ["apple", "cherry"]

# ⚠️ Nếu xóa phần tử không tồn tại → lỗi!
fruits.remove("grape")  # ValueError: list.remove(x): x not in list
```

#### .pop(index) — Xóa theo vị trí, trả về giá trị

```python
fruits = ["apple", "banana", "cherry"]

# Xóa phần tử ở index 0 (apple), trả về "apple"
removed = fruits.pop(0)
print(removed)   # "apple"
print(fruits)    # ["banana", "cherry"]

# Xóa phần tử cuối (pop không có argument = xóa cuối)
last = fruits.pop()
print(last)      # "cherry"
print(fruits)    # ["banana"]

# Xóa phần tử ở index -1 (cuối cùng)
fruits = ["apple", "banana", "cherry"]
fruits.pop(-1)
print(fruits)    # ["apple", "banana"]
```

**So sánh:**
| Phương thức | Xóa theo | Trả về | Lỗi khi không tìm thấy |
|---|---|---|---|
| `.remove(value)` | Giá trị | Không | ValueError |
| `.pop(index)` | Vị trí | Giá trị bị xóa | IndexError |

---

### 1.7 Tóm tắt Phần 1

```python
# Tạo
fruits = ["apple", "banana", "cherry"]

# Truy cập
print(fruits[0])      # "apple"
print(fruits[-1])     # "cherry"

# Cắt
print(fruits[0:2])    # ["apple", "banana"]

# Thêm
fruits.append("orange")

# Xóa
fruits.remove("banana")   # xóa theo giá trị
fruits.pop(0)             # xóa theo vị trí
```

---

## 📌 PHẦN 2: SORTED & REVERSED

### 2.1 sorted() — Sắp xếp (tạo list mới)

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sorted() trả về LIST MỚI được sắp xếp
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

# ⚠️ List gốc KHÔNG thay đổi
print(numbers)         # [3, 1, 4, 1, 5, 9, 2] (vẫn nguyên)
```

**Sắp xếp từ cao đến thấp:**

```python
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  # [9, 5, 4, 3, 2, 1, 1]
```

**Sắp xếp chữ (theo thứ tự alphabet):**

```python
words = ["zebra", "apple", "mango", "banana"]
sorted_words = sorted(words)
print(sorted_words)  # ['apple', 'banana', 'mango', 'zebra']
```

---

### 2.2 reversed() — Đảo ngược (tạo iterator)

```python
numbers = [1, 2, 3, 4, 5]

# reversed() trả về ITERATOR (không phải list)
# Cần convert thành list bằng list()
reversed_list = list(reversed(numbers))
print(reversed_list)  # [5, 4, 3, 2, 1]

# ⚠️ List gốc KHÔNG thay đổi
print(numbers)        # [1, 2, 3, 4, 5] (vẫn nguyên)
```

---

### 2.3 .sort() & .reverse() — Thay đổi list gốc (In-place)

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# .sort() — sắp xếp LIST GỐC (thay đổi vĩnh viễn!)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Không trả về gì cả (None)
result = numbers.sort()
print(result)   # None
```

```python
numbers = [1, 2, 3, 4, 5]

# .reverse() — đảo ngược LIST GỐC
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

---

### 2.4 So sánh: sorted/reversed vs .sort/.reverse

| | sorted() | .sort() |
|---|---|---|
| **Tạo list mới hay thay đổi gốc?** | Tạo mới | Thay đổi gốc |
| **Trả về gì?** | List mới | None |
| **List gốc?** | Không thay đổi | Thay đổi vĩnh viễn |
| **Dùng khi nào?** | Cần giữ nguyên list gốc | Chắc chắn muốn thay đổi |

---

### 2.5 Tóm tắt Phần 2

```python
# Tạo list mới (không thay đổi gốc)
sorted_asc = sorted(numbers)          # từ nhỏ → lớn
sorted_desc = sorted(numbers, reverse=True)  # từ lớn → nhỏ
reversed_list = list(reversed(numbers))

# Thay đổi list gốc
numbers.sort()        # sắp xếp gốc
numbers.reverse()     # đảo ngược gốc
```

---

## 📌 PHẦN 3: LIST COMPREHENSION (★ RẤT QUAN TRỌNG!)

### 3.1 Khái niệm

**List comprehension** là cách **gọn gàng** để tạo list mới từ list cũ.

Thay vì viết:
```python
# Cách cũ (dài dòng)
squared = []
for num in [1, 2, 3, 4, 5]:
    squared.append(num ** 2)
```

Viết:
```python
# Cách mới (gọn gàng!)
squared = [num ** 2 for num in [1, 2, 3, 4, 5]]
```

---

### 3.2 Cú pháp cơ bản

#### **Dạng 1: Transform (áp dụng phép toán)**

```
[biểu_thức for item in list]
```

**Ví dụ:**
```python
numbers = [1, 2, 3, 4, 5]

# Bình phương mỗi số
squared = [num ** 2 for num in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# Nhân đôi
doubled = [num * 2 for num in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# Chuyển chữ thành chữ hoa
words = ["hello", "world"]
upper = [word.upper() for word in words]
print(upper)    # ['HELLO', 'WORLD']
```

---

#### **Dạng 2: Filter (lọc phần tử)**

```
[biểu_thức for item in list if điều_kiện]
```

**Ví dụ:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lấy chỉ số chẵn
even = [num for num in numbers if num % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]

# Lấy chỉ số lẻ
odd = [num for num in numbers if num % 2 != 0]
print(odd)   # [1, 3, 5, 7, 9]

# Lấy chỉ số > 5
greater_than_5 = [num for num in numbers if num > 5]
print(greater_than_5)  # [6, 7, 8, 9, 10]
```

---

#### **Dạng 3: Transform + Filter (cả hai cùng lúc)**

```
[biểu_thức for item in list if điều_kiện]
```

**Ví dụ:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lấy số chẵn rồi bình phương
even_squared = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squared)  # [4, 16, 36, 64, 100]

# Lấy số > 5 rồi nhân 10
over_5_times_10 = [num * 10 for num in numbers if num > 5]
print(over_5_times_10)  # [60, 70, 80, 90, 100]
```

---

### 3.3 Ứng dụng thực tế

#### **1. Lọc dữ liệu từ API**

```python
# Giả sử API trả danh sách sản phẩm
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 30},
    {"name": "Monitor", "price": 400}
]

# Lấy chỉ tên sản phẩm giá > 100
expensive_names = [p["name"] for p in products if p["price"] > 100]
print(expensive_names)  # ['Laptop', 'Monitor']
```

#### **2. Chuyển đổi dữ liệu**

```python
# Danh sách tên
names = ["alice", "bob", "charlie"]

# Chuyển thành chữ hoa
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']
```

#### **3. Tính toán với từng phần tử**

```python
# Giá gốc
prices = [29.99, 15.50, 42.00]

# Áp dụng discount 10%
discounted = [round(p * 0.9, 2) for p in prices]
print(discounted)  # [27.0, 14.0, 37.8]
```

---

### 3.4 Tại sao list comprehension quan trọng?

1. **Gọn gàng:** Thay vì 3-4 dòng → 1 dòng duy nhất
2. **Nhanh:** List comprehension nhanh hơn for loop thường
3. **Chuyên nghiệp:** Công ty Đức (nơi bạn muốn làm) yêu cầu code gọn, dễ đọc
4. **Được dùng mọi nơi:** REST API, database queries, data processing

---

### 3.5 Tóm tắt Phần 3

```python
# Transform
[expr for item in list]

# Filter
[expr for item in list if condition]

# Transform + Filter
[expr for item in list if condition]
```

---

## 📌 BONUS: EXTEND vs APPEND

### 4.1 Khác nhau cơ bản

```python
# APPEND — thêm toàn bộ như 1 phần tử
list1 = [1, 2, 3]
list1.append([4, 5, 6])
print(list1)  # [1, 2, 3, [4, 5, 6]]  ❌ LỒ NHAU!

# EXTEND — thêm từng phần tử một
list2 = [1, 2, 3]
list2.extend([4, 5, 6])
print(list2)  # [1, 2, 3, 4, 5, 6]  ✅ PHẲNG!
```

---

### 4.2 Khi nào dùng cái nào?

| Tình huống | Dùng gì | Ví dụ |
|---|---|---|
| Thêm 1 phần tử đơn | `.append()` | `list.append(5)` |
| Thêm 1 object (list, dict) | `.append()` | `list.append([1,2,3])` |
| Merge 2 list thành 1 | `.extend()` | `list1.extend(list2)` |
| Thêm nhiều phần tử từ iterable | `.extend()` | `list.extend([1,2,3])` |

---

### 4.3 Extend với các kiểu dữ liệu khác

```python
# Extend với string (string = iterable)
list1 = ['a', 'b']
list1.extend("XY")
print(list1)  # ['a', 'b', 'X', 'Y']

# Extend với tuple
list2 = [1, 2]
list2.extend((3, 4, 5))
print(list2)  # [1, 2, 3, 4, 5]

# Extend với range
list3 = []
list3.extend(range(3))
print(list3)  # [0, 1, 2]
```

---

## 🎯 TÓNG TẮT TOÀN BÀI

### Những gì bạn đã học:

| Phần | Kỹ năng | Ứng dụng |
|---|---|---|
| **1** | List cơ bản, indexing, slicing, append, remove, pop | Quản lý danh sách dữ liệu |
| **2** | sorted(), reversed(), .sort(), .reverse() | Sắp xếp và đảo ngược dữ liệu |
| **3** | **List comprehension** (★) | Transform, filter dữ liệu gọn gàng |
| **Bonus** | .extend() vs .append() | Merge danh sách đúng cách |

---

## ⚡ NHỮNG LỖI THƯỜNG GẶP

### Lỗi 1: Quên rằng index bắt đầu từ 0

```python
# ❌ SAI
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Mong muốn "apple" nhưng lại là "banana"

# ✅ ĐÚNG
print(fruits[0])  # "apple"
```

---

### Lỗi 2: Dùng .append() thay vì .extend() để merge list

```python
# ❌ SAI
list1 = [1, 2, 3]
list1.append([4, 5, 6])
print(list1)  # [1, 2, 3, [4, 5, 6]]  — LỒ NHAU!

# ✅ ĐÚNG
list1 = [1, 2, 3]
list1.extend([4, 5, 6])
print(list1)  # [1, 2, 3, 4, 5, 6]  — PHẲNG!
```

---

### Lỗi 3: Typo trong tên biến

```python
# ❌ SAI
students = ["Alice", "Bob"]
print(Studnets)  # NameError: name 'Studnets' is not defined (thiếu 't')

# ✅ ĐÚNG
print(students)  # Đúng tên biến
```

---

### Lỗi 4: Nhầm sorted() với .sort()

```python
# sorted() — tạo list mới
result = sorted([3, 1, 2])
print(result)  # [1, 2, 3]

# .sort() — thay đổi list gốc, trả về None
numbers = [3, 1, 2]
result = numbers.sort()
print(result)  # None  ← Đánh lừa!
print(numbers)  # [1, 2, 3]  ← List gốc đã thay đổi
```

---

### Lỗi 5: Slice đếm sai khoảng

```python
numbers = [10, 20, 30, 40, 50]

# ❌ SAI — Mong [10, 20, 30] nhưng lại là [10, 20]
print(numbers[0:2])  # [10, 20]  ← end=2 không bao gồm index 2

# ✅ ĐÚNG
print(numbers[0:3])  # [10, 20, 30]  ← end=3 bao gồm index 0, 1, 2
```

---

## 💡 LỜI KHUYÊN CHO LẬP TRÌNH VIÊN FIAE

1. **List comprehension là SKILL BẮT BUỘC** — Dùng nó hàng ngày trong công việc thực
2. **Hiểu rõ index** — Lỗi off-by-one rất phổ biến trong lập trình
3. **Biết khi nào tạo mới, khi nào thay đổi gốc** — Quan trọng cho performance
4. **Test với danh sách rỗng, 1 phần tử, nhiều phần tử** — Edge cases rất quan trọng
5. **Đọc code của người khác** — Bạn sẽ thấy list comprehension được dùng rất nhiều

---

## 📚 REFERENCE NHANH

```python
# KHỞI TẠO
my_list = [1, 2, 3]
empty = []

# TRUY CẬP
my_list[0]      # Phần tử đầu
my_list[-1]     # Phần tử cuối
my_list[0:3]    # Slice

# THAY ĐỔI
my_list.append(4)           # Thêm vào cuối
my_list.remove(2)           # Xóa theo giá trị
my_list.pop(0)              # Xóa theo index
my_list.extend([5, 6])      # Merge list

# SẮP XẾP
sorted(my_list)             # Tạo list mới (sắp xếp)
sorted(my_list, reverse=True)  # Từ lớn đến nhỏ
my_list.sort()              # Thay đổi gốc

# ĐẢO NGƯỢC
list(reversed(my_list))     # Tạo list mới
my_list.reverse()           # Thay đổi gốc

# LIST COMPREHENSION
[x**2 for x in my_list]                 # Transform
[x for x in my_list if x > 2]           # Filter
[x**2 for x in my_list if x > 2]        # Transform + Filter
```

---

**Bạn đã sẵn sàng cho Buổi 9: Conditional Logic (if/elif/else) chưa? 🚀**
