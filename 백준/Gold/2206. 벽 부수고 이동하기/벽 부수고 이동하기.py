from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS(queue):
    condition = False
    while queue:
        y, x, check = queue.popleft()
        if y == N - 1 and x == M - 1:
            condition = True
            print(visited[y][x][check])
            break
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0 and visited[ny][nx][check] == 0:
                    visited[ny][nx][check] = visited[y][x][check] + 1
                    queue.append((ny, nx, check))

                elif graph[ny][nx] == 1 and check == 0:
                    visited[ny][nx][check+1] = visited[y][x][check] + 1
                    queue.append((ny, nx, check + 1))

    if not condition:
        print(-1)


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
queue = deque([(0, 0, 0)])

visited[0][0][0] = 1
BFS(queue)
