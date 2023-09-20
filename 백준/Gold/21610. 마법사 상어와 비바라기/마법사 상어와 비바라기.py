import sys
input = sys.stdin.readline

# 비바라기와 물복사 버그 델타
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [-1, -1, 1, 1]
dx = [-1, 1, 1, -1]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

# 처음 구름의 위치
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 이동 명령
for _ in range(M):
    d, s = map(int, input().split())

    # 이동한 구름의 위치와 비
    move_cloud = []
    for r, c in cloud:
        nr = (r + s * dr[d-1]) % N
        nc = (c + s * dc[d-1]) % N
        # 구름 이동 후 이동 구름 좌표에 물 + 1
        graphs[nr][nc] += 1
        move_cloud.append((nr, nc))

    # 물 복사
    for r, c in move_cloud:
        copy = 0
        for delta in range(4):
            nr = r + dy[delta-1]
            nc = c + dx[delta-1]
            if 0<=nr<N and 0<=nc<N:
                if graphs[nr][nc]:
                    copy += 1
        graphs[r][c] += copy

# - - - - - - - - - - 1 이동 후 새로운 이동 - - - - - - - - - -

    ncloud = []
    for y in range(N):
        for x in range(N):
            # 이동 구름 좌표 X & 값이 2 이상인 바구니
            if (y, x) not in move_cloud and graphs[y][x] >= 2:
                graphs[y][x] -= 2
                ncloud.append((y, x))
    cloud = ncloud

# - - - - - - - - - - M 이동 후 물 양 계산 - - - - - - - - - -

answer = 0
for y in range(N):
    for x in range(N):
        answer += graphs[y][x]

print(answer)