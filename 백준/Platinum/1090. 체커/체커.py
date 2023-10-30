# 모든 위치에서 모든 지점의 거리를 다 구해보자고~
# row, col 따로 거리 계산해서 합치기!
# 근데 이거 최소거리 다 구하면 좀 구질쓰,,,

# 대충 가운데 지점의 거리기준으로 최소를 구하면 될 듯..?
# 소트 때려서 홀수일땐 가운데 집하고
# 짝수면 중간집 , 중간집 -1 하면 될 듯?


# 모든 위치에서 모든 지점의 거리를 다 구해보자고~
# row, col 따로 거리 계산해서 합치기!
# 근데 이거 최소거리 다 구하면 좀 구질쓰,,,

# 대충 가운데 지점의 거리기준으로 최소를 구하면 될 듯..?
# 소트 때려서 홀수일땐 가운데 집하고
# 짝수면 중간집 , 중간집 -1 하면 될 듯?


n = int(input())
x = []
y = []
result = [-1] * n

for _ in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

for i in x:
    for j in y:
        # 체커가 있는 위치에서 다른 좌표로의 거리 계산
        dist = []
        for k in range(n):
            dist.append(abs(x[k] - i) + abs(y[k] - j))

        # 가까운 순으로 정렬하기
        dist.sort()

        # m개의 체커가 같은 곳에 모일 때의 최소 비용을 계산
        tmp = 0
        for m in range(len(dist)):
            d = dist[m]
            tmp += d
            if result[m] == -1:
                result[m] = tmp
            else:
                result[m] = min(tmp, result[m])

print(*result)