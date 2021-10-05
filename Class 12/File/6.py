def count1(filename):
    file = open(filename, "r")
    sentences = file.readlines()
    vowels = 0
    consonants = 0
    for sentence in sentences:
        for character in sentence:
            if character.lower() in ["a", "e", "i", "o", "u"]:
                vowels += 1
            else:
                consonants += 1
    file.close()
    print("Number of vowels is: ", vowels)
    print("Number of consonants is: ", consonants)


def count2(filename):
    file = open(filename, "r")
    vowels = 0
    consonants = 0

    character = " "

    while character:
        character = file.read(1)
        if character.lower() in ["a", "e", "i", "o", "u"]:
            vowels += 1
        else:
            consonants += 1

    file.close()
    print("Number of vowels is: ", vowels)
    print("Number of consonants is: ", consonants)


count1("6.txt")
count2("6.txt")
