# import csv
# print("Enter your name and roll number to see your subject marks...\n")
# name = input("Enter Name exactly as in Hall Ticket: ")
# rollno = input("Enter Roll No.: ")
# with open('student_marks.csv') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter=',')
# 	line_count = 0
# 	match_found = False
# 	for row in csv_reader:
# 		line_count += 1
# 		if line_count == 1:
# 			continue
# 		else:
# 			if row[0].lower() == name.lower() and row[1] == rollno:
# 				match_found = True
# 				eng_marks = row[3]
# 				maths_marks = row[4]
# 				cs_marks = row[5]
# 				print("\n"+row[0]+"'s marks are:\nEnglish:",eng_marks)
# 				print("Maths:", maths_marks, "\nComp Sc:", cs_marks,"\n\nThank you!")
# 				break
# 	if match_found == False:
# 		print ("\nNo matching name and roll number found. Please check and re-enter")

txt = "How are you, Ravi?"
x = txt.find(",")
y = txt.find("?")
print(x)
print(txt[x+2:y])