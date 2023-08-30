N = [int(input()) for _ in range(3)]
result = str(N[0]*N[1]*N[2])
answer = [0]*10

for digit in result:
    answer[int(digit)] += 1

for idx in range(10):
    print(answer[idx])
