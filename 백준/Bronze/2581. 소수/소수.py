M = int(input())
N = int(input())

result = []

for number in range(M, N+1):
    condition = True
    if number >= 2:
        for div in range(2, int(number**0.5 + 1)):
            if number % div == 0:
                condition = False
                break
        if condition:
            result.append(number)


if len(result):
    print(sum(result))
    print(result[0])
else:
    print(-1)