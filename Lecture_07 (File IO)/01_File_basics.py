# first we have to open file before reading and writing.

# SYNTAX: f = open("file_name", "mode")  if mode is not written then by default it will open in read mode

f = open("demo.txt", "r")

data = f.read()
print(data)

print(type(data))

f.close()


# ------------- MODES OF OPENING A FILE: -------------

# 1. "r"    :   open for reading (default)
# 2. "w"    :   open for writing, truncating(removes existing data) the file first
# 3. "x"    :   create a new file and open it for writing
# 4. "a"    :   open for writing, appending to the end of the file if it exists
# 5. "b"    :   binary code
# 6. "t"    :   text mode (default)
# 7. "+"    :   open a disk file for updating (reading and writing)

# METHODS of reading a  file

data = f.read(5)  # reads 5 characters from start
data = f.readline() # reads one line at a time