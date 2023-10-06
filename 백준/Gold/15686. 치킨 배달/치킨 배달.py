# import sys
# from itertools import combinations

# input = sys.stdin.readline

# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
# result = float('inf')
# houses = []
# chicks = []

# for i in range(N):
#     for i in range(N):
#         if city[i][i] == 1:
#             houses.append([i, i])
#         elif city[i][i] == 2:
#             chicks.append([i, i])

# for chicken in combinations(chicks, M):
#     temp = 0
#     for house in houses: 
#         distance = float('inf')
#         for i in range(M):
#             distance = min(distance, abs(house[0] - chicken[i][0]) + abs(house[1] - chicken[i][1]))
#         temp += distance
#     result = min(result, temp)

# print(result)

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

num_chicken = 0

# 집 저장하기
home_list = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            num_chicken += 1

        elif city[i][j] == 1:
            home_list.append((i, j))


ans = 1e9

def get_chicken_dist(chicken_list, home_list):


    ck_sum = 0
    for i in home_list:
        ckmindist = 1e9
        for ck in chicken_list:
            val = abs(ck[0] - i[0]) + abs(ck[1] - i[1])
            ckmindist = min(ckmindist, val)
        ck_sum += ckmindist
    return ck_sum



def dfs(ans, arr, cnt, sr, y, home_list):
    if cnt == M:
        chicken_list = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    chicken_list.append((i, j))

        return get_chicken_dist(chicken_list, home_list)

    for i in range(sr, N):

        if sr == i:
            sc = y
        else:
            sc = 0
        for j in range(sc, N):
            if arr[i][j] == 2:
                arr[i][j] = 0

                ans = min(ans, dfs(ans, arr, cnt-1, i, j+1, home_list))

                arr[i][j] = 2

    return ans

ans = dfs(ans, city, num_chicken, 0, 0, home_list)
print(ans)

