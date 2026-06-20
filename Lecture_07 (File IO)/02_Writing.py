f = open("demo.txt", "a+")
f.write("\nI am the boss")

f.seek(0)
data = f.read()
print(data)

f.close()