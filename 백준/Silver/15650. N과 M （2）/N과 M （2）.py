import sys

input = sys.stdin.readline


def DFS(depth, i):
    if depth == M:
        print(*result)
        return
    else:
        for j in range(i+1, N+1):
            if not visited[j]:
                visited[j] = True
                result.append(j)
                DFS(depth+1, j)
                visited[j] = False
                result.pop()
    return


N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []

DFS(0, 0)