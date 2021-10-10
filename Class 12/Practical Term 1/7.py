def copy():
    file = open("data.txt", "r")
    outfile = open('outdata.txt', 'w')
    data = file.read()
    words = data.split(" ")
    for word in words:
        if len(word) > 1 and word[:2] == "th":
            outfile.write(word)
    file.close()
    outfile.close()


copy()
