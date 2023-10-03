from collections import deque

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def find(swan_cur_pos, swan, visited, graph):
    swan_nxt_pos = deque()
    while swan_cur_pos:
        y, x = swan_cur_pos.popleft()

        if y == swan[1][0] and x == swan[1][1]:
            return True, None

        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == False:
                if graph[ny][nx] == 'X':
                    swan_nxt_pos.append([ny, nx])
                else:
                    swan_cur_pos.append([ny, nx])

                visited[ny][nx] = True

    return False, swan_nxt_pos


def melt(lake, graph):
    melt_lake = deque()

    while lake:
        y, x = lake.popleft()

        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c:
                if graph[ny][nx] == 'X':
                    melt_lake.append([ny, nx])
                    graph[ny][nx] = '.'

    return melt_lake


def solution(graph):
    lake = deque()
    swan = []
    day = -1
    visited = [[False for _ in range(c)] for _ in range(r)]

    for row in range(r):
        for col, val in enumerate(graph[row]):
            if val == '.' or val == 'L':
                lake.append([row, col])
            if val == 'L':
                swan.append([row, col])

    swan_cur_pos = deque()
    y, x = swan[0][0], swan[0][1]
    swan_cur_pos.append([y, x])
    visited[y][x] = True

    while True:
        day += 1
        found_flag, swan_nxt_pos = find(swan_cur_pos, swan, visited, graph)
        if found_flag: 
            break
        lake = melt(lake, graph)
        swan_cur_pos = swan_nxt_pos

    return day


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]


print(solution(graph))