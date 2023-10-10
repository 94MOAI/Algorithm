delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def BFS(queue):
    while queue:
        y, x = queue.pop(0)
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = []
for y in range(N):
    for x in range(M):
        if graph[y][x]:
            queue.append((y, x))

BFS(queue)

mx_dist = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] >= mx_dist:
            mx_dist = graph[y][x]

print(mx_dist-1)