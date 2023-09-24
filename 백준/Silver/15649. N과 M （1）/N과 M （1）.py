def f(i, N, M):
    if i == M:
        print(*p)
        return
    else:
        for j in range(N):
            if not used[j]:
                p[i] = num[j]
                used[j] = 1
                f(i+1, N, M)
                used[j] = 0


N, M = map(int, input().split())

num = [i for i in range(1, N+1)]

p = [0] * M
used = [0] * N

f(0, N, M)