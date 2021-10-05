import pickle


def writeData(filename):
    file = open(filename, "wb")

    char = "y"

    while char == "y":
        emp = {}
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        emp["name"] = name
        emp["age"] = age
        pickle.dump(emp, file)
        char = input("Do you want to continue? (y/n) ")

    file.close()


def readData(filename):
    file = open("emp.dat", "rb")

    try:
        while True:
            print(pickle.load(file))
    except EOFError:
        print("End of file")

    file.close()


# writeData("emp.dat")
# readData("emp.dat")
