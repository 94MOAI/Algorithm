stack = []
result = []

N = int(input())

element = 1
condition = True

for _ in range(N):
    num = int(input())
    while element <= num:
        stack.append(element)
        result.append('+')
        element += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        condition = False
        break

if condition:
    for operater in result:
        print(operater)