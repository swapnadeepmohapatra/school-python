def readFirst30Chars(fileName):
    file = open(fileName, "r")
    print(file.read(30))
    file.close()


def readFirst30Then50(filename):
    file = open(filename, "r")
    print(file.read(30))
    print(file.read(50))
    file.close()


def readEntireContent(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()


def readFileLineByLine1(filename):
    file = open(filename, "r")
    str = " "
    while str:
        str = file.readline()
        print(str, end="")

    file.close()


def readFileLineByLine2(filename):
    file = open(filename, "r")
    for line in file:
        print(line, end="")

    file.close()


def readingFileInALine(filename):
    file = open(filename, "r")
    print(file.readlines())
    file.close()


# readFirst30Chars("1.txt")
# readFirst30Then50("1.txt")
# readEntireContent("1.txt")
# readFileLineByLine1("1.txt")
# readFileLineByLine2("1.txt")
# readingFileInALine("1.txt")
