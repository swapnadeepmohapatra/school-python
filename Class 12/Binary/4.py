import pickle


def searchByName(filename):
    file = open(filename, "rb")
    name_in = input("Input name: ")
    found = False
    try:
        while True:
            data = pickle.load(file)
            if(data["name"] == name_in):
                print(data)
                found = True
    except EOFError:
        if not found:
            print("Entry Not Found")


searchByName("emp.dat")
