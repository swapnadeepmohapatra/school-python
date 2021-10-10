def cube(n=2):
    print(n**3)


cube(3)
cube()


def twoChars(a, b):
    if a == b:
        return True
    else:
        return False


print(twoChars("a", "b"))
print(twoChars("d", "d"))
