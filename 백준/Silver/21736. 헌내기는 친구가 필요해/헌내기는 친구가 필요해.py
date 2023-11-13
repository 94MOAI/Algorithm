def bfs(s):
    global answer
    while s:
        y, x = s.pop(0)
        for dy, dx in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M:
                if maps[ny][nx] == 'P':
                    answer +=1
                    maps[ny][nx] = 'X'
                    s.append([ny,nx])
                elif maps[ny][nx] == 'O':
                    maps[ny][nx] = 'X'
                    s.append([ny, nx])


N, M = map(int, input().split())
maps = [list(input())for _ in range(N)]

flag = False
for y in range(N):
    for x in range(M):
        if maps[y][x] == 'I':
            s = [[y, x]]
            maps[y][x] = 'X'
            flag = True
            break
    if flag:
        break

answer = 0
bfs(s)
if not answer:
    print("TT")
else:
    print(answer)
