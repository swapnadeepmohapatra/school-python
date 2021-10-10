f = open("data.txt", 'w')
f.write("Hello")
f.write("Welcome to my Blog")
f.close()
f = open("data.txt", 'r')
d = f.read(5)
print(d)  # First Print Statement
f.seek(10)
d = f.read(3)
print(d)  # Second Print Statement
f.seek(13)
d = f.read(5)
print(d)  # Third Print Statement
d = f.tell()
print(d)  # Fourth Print Statement
