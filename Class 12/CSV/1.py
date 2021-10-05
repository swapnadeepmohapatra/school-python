import csv

with open('data.csv', 'w', newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Phone'])
    char = "y"
    list_of_data = []
    while char == "y":
        input_data_name = input("Enter Name: ")
        input_data_phone = input("Enter Phone: ")
        list_of_data.append([input_data_name, input_data_phone])
        char = input("More data y/n: ")

    csv_writer.writerows(list_of_data)
