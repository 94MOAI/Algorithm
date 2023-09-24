# 조합 응용

def f(depth, index):
    if depth == M:
        print(*subset)
        return
    for i in range(index, N+1):
        subset.append(i)
        used[i] = 1
        f(depth+1, i)
        subset.pop()
        used[i] = 0



N, M = map(int, input().split())
used = [0] * (N+1)
subset = []
f(0, 1)