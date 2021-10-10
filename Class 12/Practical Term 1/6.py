data_out = ""
with open("file.txt", "r") as test_file:
    data = test_file.readline()

    while(data):
        if(data.find("a") == -1):
            data_out += data
        data = test_file.readline()

with open("test_res.txt", "w")as test_file2:
    test_file2.write(data_out)
