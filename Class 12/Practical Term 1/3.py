def addDict(dict1, dict2):
    new_dic = {}
    for i in dict1.keys():
        new_dic[i] = dict1[i]

    for i in dict2.keys():
        new_dic[i] = dict2[i]

    return new_dic


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "e": 6}

print(addDict(dict1, dict2))
