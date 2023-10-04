list1 = list(map(int, input()))
N = len(list1)
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
if list1[0] == 0:
    print(0)
else:
    for i in range(1, N):
        if list1[i] > 0:
            dp[i+1] += dp[i]
        tmp = list1[i-1]*10 + list1[i]
        if tmp >= 10 and tmp <= 26:
            dp[i+1] += dp[i-1]
        dp[i+1] %= 1000000
    print(dp[N])