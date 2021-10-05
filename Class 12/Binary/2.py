import pickle


def appendMoreData(filename):
    file = open(filename, "ab")
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


appendMoreData("emp.dat")
