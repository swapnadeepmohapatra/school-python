stack = []


def isEmpty(stk):
    return stk == []


def push(stk, item):
    stk.append(item)


def pop(stk):
    if isEmpty(stk):
        print("[Underflow] Stack is empty")
        return None

    return stk.pop()


def peek(stk):
    if isEmpty(stk):
        print("Stack is empty")
    else:
        print(stk[len(stk)-1])


def size(stk):
    return len(stk)


peek(stack)
print(size(stack))
push(stack, 10)
push(stack, 12)
push(stack, 15)
peek(stack)
print(size(stack))
print(pop(stack))
peek(stack)
print(size(stack))
