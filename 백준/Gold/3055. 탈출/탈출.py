# 비어있는 곳 : .
# 물이 차있는 지역 : *
# 돌 : X
# 비버의 굴 : D
# 고슴도치의 위치 : S

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

def BFS(sy, sx):
    queue = [(sy, sx)]
    visited[sy][sx] = 1
    cnt = 0

    while queue:
        cnt += 1

        water = []
        for y in range(R):
            for x in range(C):
                if maps[y][x] == '*' and not visited[y][x]:
                    water.append((y, x))
                    visited[y][x] = 1
        for y, x in water:
            for dy, dx in delta:
                ny, nx = y + dy, x + dx
                if 0<=ny<R and 0<=nx<C and not visited[ny][nx]:
                    if maps[ny][nx] == '.':
                        maps[ny][nx] = '*'

        for _ in range(len(queue)):
            y, x = queue.pop(0)
            for dy, dx in delta:
                ny, nx = y + dy, x + dx
                if 0<=ny<R and 0<=nx<C and not visited[ny][nx]:
                    if maps[ny][nx] == '.':
                        queue.append((ny, nx))
                        visited[ny][nx] = 1
                    elif maps[ny][nx] == 'D':
                        return cnt

    return 'KAKTUS'


R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

visited = [[0]*C for _ in range(R)]
sy, sx = 0, 0
for y in range(R):
    for x in range(C):
        if maps[y][x] == 'S':
            sy, sx = y, x
            maps[y][x] = '.'

print(BFS(sy, sx))