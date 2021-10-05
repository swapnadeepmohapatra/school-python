import pickle


def readEmpData(filename):
    with open(filename, "rb") as file:
        try:
            while True:
                data = pickle.load(file)
                print(data)
        except EOFError:
            pass


readEmpData("emp.dat")
