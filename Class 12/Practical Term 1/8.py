def readFileLineByLine2():
    file = open("article.txt", "r")
    data = file.readlines()
    for line in data:
        words = line.split(" ")
        print("First word:", words[0])
        print("Last word:", words[len(words) - 1])


readFileLineByLine2()
