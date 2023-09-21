from collections import deque

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def BFS(s, e):
    queue = deque()
    queue.append((s, e))

    while queue:
        y, x = queue.popleft()
        for dy, dx in delta:
            ny, nx = dy + y, dx + x
            if 0 <= ny < N and 0 <= nx < N:
                extra = 1
                if graph[ny][nx] > graph[y][x]:
                    extra += graph[ny][nx] - graph[y][x]
                if cost[ny][nx] > cost[y][x] + extra:
                    cost[ny][nx] = cost[y][x] + extra
                    queue.append((ny, nx))


for test_case in range(1, int(input())+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    cost = [[float('inf')]*N for _ in range(N)]
    cost[0][0] = 0
    BFS(0,0)


    print(f'#{test_case} {cost[N - 1][N - 1]}')