def writeStringData(filename):
    file = open(filename, "w")
    file.write("Hwello")
    file.close()


def writeListData(filename):
    file = open(filename, "w")
    file.writelines(["Hello", "Hey", "Bye"])
    file.close()


def writeNames(filename):
    file = open(filename, "w")
    names = []
    char = "y"
    while char == "y":
        name = input("Enter Name: ")
        names.append(name + "\n")
        char = input("Want more data? y/n ")

    file.writelines(names)
    file.close()


def writeStudentsData(filename):
    file = open(filename, "w")
    char = "y"
    while char == "y":
        name = input("Enter Name: ")
        roll = input("Enter Roll No.: ")
        marks = input("Enter Marks: ")

        record = roll+", "+name+", "+marks+"\n"
        file.write(record)

        char = input("You wanna put more? y/n")
    file.close()


# writeStringData("3.txt")
# writeListData("3.txt")
# writeNames("3.txt")
writeStudentsData("3.txt")
