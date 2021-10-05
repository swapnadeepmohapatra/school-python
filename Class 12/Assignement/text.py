# my_file = open("text.txt", "r")
# print(my_file.read(100))


obj1 = open("text.txt", "r")
s1 = obj1.readline()
# s2.readline(10)
s2 = obj1.readline(10)
s3 = obj1.read(15)
print(s1)
print(s2)
print(s3)
print(obj1.readline())
obj1.close()
