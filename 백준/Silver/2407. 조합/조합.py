def factorial(n):
    for i in range(1,n+1):
        dp[i] = dp[i-1] * i
    return dp

N, M = map(int, input().split())
dp = [0]*(N+1)
dp[0] = 1
factorial(N)

answer = dp[N]//(dp[M]*dp[N-M])
print(answer)