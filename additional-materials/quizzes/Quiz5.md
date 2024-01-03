# Quiz5.md

## Python Advanced Data Structures Quiz

This quiz is designed to test your knowledge of advanced data structures in Python, such as list comprehensions, sets, and dictionaries. These structures are key to efficient data handling and manipulation in Python.

---

**Question 1:** Which of the following is a correct list comprehension in Python?

1. `squares = [for i in range(10): i*i]`
2. `squares = [i*i for i in range(10)]`
3. `squares = list(i*i for i in range(10))`
4. Both 2 and 3

**Answer:** 4. Both 2 and 3

---

**Question 2:** What will be the output of the following code?

```python
my_set = {1, 2, 3, 4, 5}
my_set.add(3)
print(len(my_set))
```

1. `4`
2. `5`
3. `6`
4. An error

**Answer:** 2. `5`

---

**Question 3:** How do you remove a key-value pair from a dictionary in Python?

1. `del dict[key]`
2. `dict.remove(key)`
3. `dict.delete(key)`
4. `dict.pop(key)`

**Answer:** 1. `del dict[key]` and 4. `dict.pop(key)` (Both are correct)

---

**Question 4:** What is the output of the following code snippet?

```python
fruits = ["apple", "banana", "cherry", "apple"]
unique_fruits = set(fruits)
print(unique_fruits)
```

1. `["apple", "banana", "cherry"]`
2. `["apple", "banana", "cherry", "apple"]`
3. `{"apple", "banana", "cherry"}`
4. `{"apple", "banana", "cherry", "apple"}`

**Answer:** 3. `{"apple", "banana", "cherry"}`

---

**Question 5:** Which method is used to merge two dictionaries in Python 3.5+?

1. `dict1.merge(dict2)`
2. `dict1 + dict2`
3. `dict1.update(dict2)`
4. `merge(dict1, dict2)`

**Answer:** 3. `dict1.update(dict2)`

---

**Question 6:** What does the following code do?

```python
nums = [1, 2, 3, 4, 5]
squared = {num: num*num for num in nums}
```

1. Creates a list of squares
2. Creates a set of squares
3. Creates a dictionary where each number is a key, and its square is the value
4. Causes a syntax error

**Answer:** 3. Creates a dictionary where each number is a key, and its square is the value

---

**Question 7:** What is the result of the following set operation?

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
```

1. `{1, 2, 3, 4, 5}`
2. `{3}`
3. `{1, 2, 4, 5}`
4. `{}` (an empty set)

**Answer:** 2. `{3}`

---

**Question 8:** In Python, what is the difference between a list and a tuple?

1. Lists are immutable, whereas tuples are mutable
2. Lists are ordered, whereas tuples are unordered
3. Lists can contain different types of elements, whereas tuples cannot
4. Lists are mutable, whereas tuples are immutable

**Answer:** 4. Lists are mutable, whereas tuples are immutable

---

This quiz helps in assessing your understanding of Python's advanced data structures. These structures are integral for writing efficient, clean, and Pythonic code, especially when dealing with complex data manipulation tasks.
