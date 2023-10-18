# N : 단원의 갯수, T : 가능한 총 시험공부시간
N, T = map(int, input().rsplit())

# 1. 입력
# 시험 계획을 짤 예정~
schedule = [(0, 0)]
for _ in range(N):
    # K : 단원 별 예상 공부 시간, S : 해당 단원 문제의 배점
    K, S = map(int, input().rsplit())
    schedule.append((K, S))

# 공부할 과목이 N개이므로 N개의 경우의 수를 모두 따져본다.
dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

# 2. 로직 -> 냅색문제처럼 완탐
for y in range(1, N + 1):
    for x in range(1, T + 1):
        # 전체 시간만큼 순회하면서 시간이 더 많이 걸리는 경우,
        # 새로 점수를 계산해서 더 높은 점수 갱신
        if x >= schedule[y][0]:
            if dp[y-1][x] >= dp[y-1][x-schedule[y][0]] + schedule[y][1]:
                dp[y][x] = dp[y-1][x]
            else:
                dp[y][x] = dp[y-1][x-schedule[y][0]] + schedule[y][1]
        else:
            # 시간이 더 적게 걸리는 경우는 그 전의 시간의 score 이어받기
            dp[y][x] = dp[y - 1][x]

# 3. 출력
print(dp[N][T])
