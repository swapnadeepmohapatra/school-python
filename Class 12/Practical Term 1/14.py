import csv
file1 = open("in.csv", "r")
file2 = open("out.csv", "w", newline="")

writer = csv.writer(file2, delimiter="|")

data = csv.reader(file1)

for i in data:
    writer.writerow(i)

file2.close()
