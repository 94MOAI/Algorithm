def factorial(N):
    if N == 0:
        return 1
    else: return N * factorial(N - 1)


N = factorial(int(input()))

N = str(N)

answer = 0
for idx in range(len(N)-1, -1, -1):
    if N[idx] == '0':
        answer += 1
    else:
        break

print(answer)