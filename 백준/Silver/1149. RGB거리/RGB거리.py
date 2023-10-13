R = 0  # 빨간색 상수
G = 1  # 초록색 상수
B = 2  # 파란색 상수

N = int(input())

# 집마다 색을 칠하게 되는 비용
houses = [list(map(int, input().split())) for _ in range(N)]

# 모든 집을 칠했을 때의 최소 비용을 계산하자...!
# dp[집번호][색상] = 지금까지의 최소비용을 계산값
dp = [[0] * 3 for _ in range(N)]

# 기저조건 : 첫 시작 집을 칠하는 비용...
dp[0][R] = houses[0][R]
dp[0][G] = houses[0][G]
dp[0][B] = houses[0][B]

# RGB 거리 문제에 점화식...
for x in range(1, N):
    dp[x][R] = min(dp[x - 1][G], dp[x - 1][B]) + houses[x][R]
    dp[x][G] = min(dp[x - 1][R], dp[x - 1][B]) + houses[x][G]
    dp[x][B] = min(dp[x - 1][R], dp[x - 1][G]) + houses[x][B]

# 최소 비용
print(min(dp[N - 1][R], dp[N - 1][G], dp[N - 1][B]))