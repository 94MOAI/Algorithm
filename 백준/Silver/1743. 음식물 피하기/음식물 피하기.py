delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

def bfs(y, x):
    result = 0
    queue = [(y, x)]
    graph[y][x] = 0

    while queue:
        y, x = queue.pop(0)
        result += 1
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 :
                    queue.append((ny, nx))
                    graph[ny][nx] = 0
    return result


N, M, K = map(int, input().split())
size = []
graph = [[0] * M for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 1


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            size.append(bfs(i, j))

print(max(size))