def change():
    infile = open('file.txt', 'r')
    outfile = open('newfile.txt', 'w')
    for line in infile:
        for letter in line:
            if letter == "i":
                outfile.write("I")
            else:
                outfile.write(letter)
    infile.close()
    outfile.close()


change()
