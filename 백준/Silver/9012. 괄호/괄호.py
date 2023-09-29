for _ in range(int(input())):
    condition = True

    braket = input()

    stack = []
    for el in braket:
        if el == '(':
            stack.append(el)
        else:
            if len(stack) == 0:
                condition = False
                print('NO')
                break
            elif stack[-1] == '(':
                stack.pop()

    if condition:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')