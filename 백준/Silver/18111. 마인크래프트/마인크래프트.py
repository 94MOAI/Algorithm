import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
idx = 0

for block in range(257):
    mx, mn = 0, 0

    for i in range(N):
        for j in range(M):

            if field[i][j] > block :
                mx += field[i][j] - block
            else : 
                mn += block - field[i][j]

    if mx + B >= mn :
        if (mx * 2) + mn <= answer:
            answer = (mx * 2) + mn
            idx = block


print(answer, idx)