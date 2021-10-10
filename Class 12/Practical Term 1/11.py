import pickle
f = open("marks.dat", "wb")

pickle.dump([1, "Arav", 99], f)
pickle.dump([2, "Brav", 88], f)
pickle.dump([3, "Crav", 77], f)
pickle.dump([4, "Drav", 66], f)
pickle.dump([5, "Erav", 55], f)

f.close()

f = open("marks.dat", "rb")
roll = int(input("Enter the Roll Number: "))
marks = float(input("Enter the updated marks: "))
List = []
flag = False
while True:
    try:
        record = pickle.load(f)
        List.append(record)
    except EOFError:
        break
f.close()

f = open("marks.dat", "wb")
for rec in List:
    if rec[0] == roll:
        rec[2] = marks
        pickle.dump(rec, f)
        print("Record updated successfully")
        flag = True
    else:
        pickle.dump(rec, f)
f.close()
if flag == False:
    print("This roll number does not exist")
