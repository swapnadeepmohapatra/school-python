def tellPositionOfALetter(filename, letter):
    file = open("7.txt", "r+")
    char = " "
    while char:
        char = file.read(1)
        if char == letter:
            print(file.tell())


tellPositionOfALetter("7.txt", "a")
