def printOutData1(filename):
    file = open(filename, "r")
    sentences = file.readlines()
    for sentence in sentences:
        for word in sentence.split(" "):
            print(word, end="#")
    file.close()


def printOutData2(filename):
    file = open(filename, "r")
    sentence = file.readline()
    for word in sentence.split(" "):
        print(word, end="#")
    file.close()


# printOutData1("5.txt") # for multiple lines
# printOutData2("5.txt") # for single line
