def main():
    infile = open('words.txt', 'r')
    outfile = open('newwords.txt', 'w')
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(chr(ord(word[0])+1) + word[1:] + " ")
        outfile.write('\n')
    infile.close()
    outfile.close()


main()
