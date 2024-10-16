def operation_pair(operation, top, prev):
    pair = {
        '+': prev + top,
        '-': prev - top,
        '*': prev * top,
        '/': prev // top
    }
    return pair[operation]

def postfix_notation(s):
    operation = "+-*/"
    stack = []
    splits = s.split()

    for char in splits:
        if char.isdigit():
            stack.append(int(char))
        elif char in operation:
            num1 = stack.pop()
            num2 = stack.pop()
            result = operation_pair(char, num1, num2)
            stack.append(result)
        else:
            return -1

    return print(stack[0])

postfix_notation("4 2 / 3 - 2 *")
postfix_notation("2 3 + 5 *")
