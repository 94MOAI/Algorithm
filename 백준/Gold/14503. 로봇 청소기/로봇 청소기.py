def f(N, M, R, C, D, maps):

    if maps[R][C] == 0:
        maps[R][C] = -1
        spot.append((R, C))

    direction = [[(0, -1), (1, 0), (0, 1), (-1, 0)], [(-1, 0), (0, -1), (1, 0), (0, 1)],
                [(0, 1), (-1, 0), (0, -1), (1, 0)], [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    for i, (dr, dc) in enumerate(direction[D]):
        if maps[R + dr][C + dc] == 0:
            R += dr
            C += dc
            D = (D + 3 - i) % 4
            return f(N, M, R, C, D, maps)

    y, x = direction[D][1]
    if maps[R + y][C + x] == 1:
        return

    elif maps[R + y][C + x] == -1:
        return f(N, M, R + y, C + x, D, maps)


N, M = map(int, input().split())
R, C, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

spot = []

f(N, M, R, C, D, maps)

print(len(spot))