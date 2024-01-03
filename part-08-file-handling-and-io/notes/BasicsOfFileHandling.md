# BasicsOfFileHandling.md

## Comprehensive Guide to File Handling in Python

File handling is an essential aspect of any programming language. In Python, file handling is easy to understand and implement. This guide covers the basics of opening, reading, writing, and closing files in Python.

---

**1. Opening Files**

- **Syntax**: `file_object = open("filename", "mode")`
- **Modes**:
  - `'r'` - Read mode (default).
  - `'w'` - Write mode (overwrites file).
  - `'a'` - Append mode (adds to the end of the file).
  - `'b'` - Binary mode (for binary files).
- **Example**:

     ```python
     f = open("example.txt", "r")
     ```

**2. Reading Files**

- **Methods**:
  - `read(size)`: Reads the file up to `size` characters.
  - `readline()`: Reads one line from the file.
  - `readlines()`: Reads all lines into a list.
- **Example**:

     ```python
     content = f.read()
     print(content)
     ```

**3. Writing to Files**

- **Methods**:
  - `write(string)`: Writes the string to the file.
  - `writelines(seq)`: Writes a sequence of strings to the file.
- **Example**:

     ```python
     f = open("example.txt", "w")
     f.write("Hello, Python!")
     ```

**4. Closing Files**

- **Importance**: It's crucial to close files to free up system resources.
- **Method**: `file_object.close()`
- **Example**:

     ```python
     f.close()
     ```

**5. The `with` Statement**

- Automatically closes the file after the nested block of code.
- **Example**:

     ```python
     with open("example.txt", "r") as f:
         print(f.read())
     ```
