# 'with' Syntax
# NOTE : using with syntax we need not to close the file as the with function automatically closes it.

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)