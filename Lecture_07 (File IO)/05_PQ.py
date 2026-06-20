# # ----------- QUESTION - 01 ----------

# f = open("practice.txt", "w")

# f.write("Hi Everyone \nwe are learning File I/O \nusing Java \nI like programming in Java")

# f.close()

# # USING 'with' FUNCTION

# with open("practice.txt", "w") as f:
#     f.write("Hi Everyone \nwe are learning File I/O \nusing Java \nI like programming in Java")

# # ----------- QUESTION - 02 ----------

f = open("practice.txt", "r")

data = f.read()
new_data = data.replace("Java", "python")
f.close()

f = open("practice.txt", "w")

f.write(new_data)
f.close

# # ----------- QUESTION - 03 ----------

f = open("practice.txt", "r")

data = f.read()

if(data.find("learning") != -1):
    print("found")
else:
    print('Not found')

f.close