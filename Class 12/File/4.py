def appendMoreDataToIt(filename):
    file = open(filename, "a")
    file.write("Hello")
    file.write("\n")
    file.close()


appendMoreDataToIt("4.txt")
