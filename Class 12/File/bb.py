def changeCase(character):
    if character.isupper():
        return character.lower()
    else:
        return character.upper()


def main():
    file_in = open("case_in.txt", "r")
    file_out = open("case_out.txt", "w")

    sentences = file_in.readlines()
    for sentence in sentences:
        for char in sentence:
            file_out.write(changeCase(char))

    file_out.close()
    file_in.close()


main()
