def sizeOfBytes(filename):
    file = open(filename, "r")
    str = file.read()
    print("Size of the file is", end=" ")
    print(len(str), "bytes")
    file.close()


def numberOfLines(filename):
    file = open(filename, "r")
    list = file.readlines()
    print("Number of lines is", end=" ")
    print(len(list))


# sizeOfBytes("2.txt")
numberOfLines("2.txt")
