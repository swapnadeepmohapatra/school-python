def printOutData1():
    file = open("file.txt", "r")
    sentences = file.readlines()
    for sentence in sentences:
        for word in sentence.split(" "):
            print(word, end="#")
    file.close()


printOutData1()
