# Quiz8.md

## Python File Handling and I/O Quiz

This quiz assesses your understanding of file handling and input/output operations in Python. It covers reading and writing files, working with different file formats, and handling file-related exceptions.

---

**Question 1:** What is the correct way to open a text file for reading in Python?

1. `open("file.txt", "r")`
2. `open("file.txt", "read")`
3. `open("file.txt")`
4. Both 1 and 3

**Answer:** 4. Both 1 and 3

---

**Question 2:** How do you ensure that a file is properly closed after finishing operations, even if an error occurs?

1. Using a `finally` block
2. Using the `with` statement
3. Calling `file.close()` at the end
4. Both 1 and 2

**Answer:** 2. Using the `with` statement

---

**Question 3:** What is the output of the following code?

```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
```

1. Writes 'Hello, World!' to 'example.txt'
2. Reads 'Hello, World!' from 'example.txt'
3. Appends 'Hello, World!' to 'example.txt'
4. Opens 'example.txt' but does nothing

**Answer:** 1. Writes 'Hello, World!' to 'example.txt'

---

**Question 4:** Which mode should you use to append data to an existing file?

1. `'r'`
2. `'w'`
3. `'a'`
4. `'rb'`

**Answer:** 3. `'a'`

---

**Question 5:** What does the following code do?

```python
file = open('example.txt', 'r')
data = file.read()
file.close()
```

1. Writes data to 'example.txt'
2. Reads data from 'example.txt' and stores it in `data`
3. Appends data to 'example.txt'
4. Deletes data from 'example.txt'

**Answer:** 2. Reads data from 'example.txt' and stores it in `data`

---

**Question 6:** How do you read a file line by line in Python?

1. Using `file.readlines()`
2. Using `file.readline()`
3. Iterating over `file`
4. Both 2 and 3

**Answer:** 4. Both 2 and 3

---

**Question 7:** What is the purpose of the `seek()` method in file handling?

1. To append data to a file
2. To move the file pointer to a specific position
3. To check the size of the file
4. To close the file

**Answer:** 2. To move the file pointer to a specific position

---

**Question 8:** What exception is raised when trying to open a non-existent file for reading?

1. `FileError`
2. `OpenError`
3. `IOError`
4. `FileNotFoundError`

**Answer:** 4. `FileNotFoundError`

---

This quiz covers key concepts in file handling and I/O operations in Python, essential for managing files effectively in any Python program. Understanding these principles is crucial for data manipulation, storage, and retrieval operations.
