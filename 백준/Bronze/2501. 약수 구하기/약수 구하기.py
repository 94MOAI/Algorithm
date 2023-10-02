N, K = map(int, input().split())

answer = []

for number in range(1, N+1):
    if N % number == 0:
        answer.append(number)

    if len(answer) == K:
        print(answer[-1])
        break
    
if len(answer) < K:
    print(0)