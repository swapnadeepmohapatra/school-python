import pickle


def addData(filename):
    f = open("stud.dat", "wb")
    pickle.dump({"roll": 1, "name": "Arav"}, f)
    pickle.dump({"roll": 2, "name": "Brav"}, f)
    pickle.dump({"roll": 3, "name": "Crav"}, f)
    pickle.dump({"roll": 4, "name": "Drav"}, f)
    pickle.dump({"roll": 5, "name": "Erav"}, f)
    f.close()


def searchByName(filename):
    file = open(filename, "rb")
    roll_in = int(input("Input roll: "))
    found = False
    try:
        while True:
            data = pickle.load(file)
            if(data["roll"] == roll_in):
                print(data["name"])
                found = True
    except EOFError:
        if not found:
            print("Entry Not Found")


addData("stud.dat")
searchByName("stud.dat")
