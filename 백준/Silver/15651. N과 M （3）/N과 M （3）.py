def f(depth):
    if depth == M:
        print(*subset)
        return

    for i in range(1, N+1):
        # if used[i]:
        #     continue
        subset.append(i)
        used[i] = 1
        f(depth+1)
        subset.pop()
        used[i] = 0




N, M = map(int, input().split())

used = [0] * (N+1)
subset = []
f(0)