T = int(input())

for test_case in range(T):
    total = int(input())
    answer = [0, 0, 0, 0]
    coin = [25, 10, 5, 1]
    for idx in range(4):
        answer[idx] += total // coin[idx]
        total %= coin[idx]

    print(*answer)