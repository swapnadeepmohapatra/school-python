def cnt():
    file = open("file.txt", "r")
    cont = file.read()

    vowels = 0
    consonants = 0
    lower_case = 0
    upper_case = 0
    for ch in cont:
        if (ch.islower()):
            lower_case += 1

        elif(ch.isupper()):
            upper_case += 1

        ch = ch.lower()

        if(ch in ['a', 'e', 'i', 'o', 'u']):
            vowels += 1

        elif (ch in ['b', 'c', 'd', 'f', 'g',
                     'h', 'j', 'k', 'l', 'm',
                     'n', 'p', 'q', 'r', 's',
                     't', 'v', 'w', 'x', 'y', 'z']):
            consonants += 1

    file.close()

    print("Vowels are : ", vowels)
    print("Consonants are : ", consonants)
    print("Lower case letters are : ", lower_case)
    print("Upper case letters are : ", upper_case)


cnt()
