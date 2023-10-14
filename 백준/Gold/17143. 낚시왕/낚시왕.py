import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
maps = [[[0, 0, 0] for _ in range(C + 1)] for _ in range(R + 1)]

for _ in range(M):
    row, col, s, d, z = map(int, input().split())
    maps[row][col] = [s, d, z]


def move(y, x, s, d):
    # 위
    if d == 1:
        if y - s >= 1:
            y -= s
        else:
            s -= y - 1
            direction = s // (R - 1)
            location = s % (R - 1)
            if direction % 2 == 0:
                d = 2
                y = 1 + location
            else:
                y = R - location

    # 아래
    elif d == 2:
        if y + s <= R:
            y += s
        else:
            s -= R - y
            direction = s // (R - 1)
            location = s % (R - 1)
            if direction % 2 == 0:
                d = 1
                y = R - location
            else:
                y = 1 + location

    # 오른쪽
    elif d == 3:
        if x + s <= C:
            x += s
        else:
            s -= C - x
            direction = s // (C - 1)
            location = s % (C - 1)
            if direction % 2 == 0:
                d = 4
                x = C - location
            else:
                x = 1 + location

    # 왼쪽
    elif d == 4:
        if x - s >= 1:
            x -= s
        else:
            s -= x - 1
            direction = s // (C - 1)
            location = s % (C - 1)
            if direction % 2 == 0:
                d = 3
                x = 1 + location
            else:
                x = C - location

    return y, x, d


def solve():
    update_maps = [[[0, 0, 0] for _ in range(C + 1)] for _ in range(R + 1)]
    for y in range(1, R + 1):
        for x in range(1, C + 1):
            if maps[y][x] != [0, 0, 0]:
                s, d, z = maps[y][x]
                ny, nx, d = move(y, x, s, d)
                update_maps[ny][nx] = max([s, d, z], update_maps[ny][nx], key=lambda x: x[2])

    return update_maps


result = 0
for time in range(1, C + 1):
    for row in range(1, R + 1):
        if maps[row][time] != [0, 0, 0]:
            result += maps[row][time][2]
            maps[row][time] = [0, 0, 0]
            break
    result_maps = solve()
    maps = [x[:] for x in result_maps]

print(result)