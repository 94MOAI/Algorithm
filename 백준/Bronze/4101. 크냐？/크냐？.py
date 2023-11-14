
while True:
    N, M = map(int, input().split())
    if N+M:
        if N > M:
            print('Yes')
        else:
            print('No')
    else:
        quit()