import csv


def addData():
    with open('user.csv', 'w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        char = "y"
        list_of_data = []
        while char == "y":
            input_data_username = input("Enter Username: ")
            input_data_password = input("Enter Password: ")
            list_of_data.append([input_data_username, input_data_password])
            char = input("More data y/n: ")

        csv_writer.writerows(list_of_data)


def searchData():
    with open('user.csv', 'r') as newFile:
        found = False
        newFileReader = csv.reader(newFile)
        username = input("Enter user name to be searched: ")
        for row in newFileReader:
            if(row[0] == username):
                found = True
                print("Password is", row[1])

        if not found:
            print("No Entry found")


addData()
searchData()
