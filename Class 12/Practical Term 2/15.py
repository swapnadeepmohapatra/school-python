stack = []


def isEmpty():
    return stack == []


def push(item):
    stack.append(item)


def pop():
    return stack.pop()


def peek():
    return stack[len(stack)-1]


def size():
    return len(stack)


print(size())
push(10)
push(12)
push(15)
print(peek())
print(size())
print(pop())
print(peek())
print(size())
