import sys

input = sys.stdin.readline

T, W = map(int, input().split())
dp = [[[0 for _ in range(W + 2)] for _ in range(T + 1)] for _ in range(2+1)]

for tree in range(1, T+1):
    N = int(input())
    for move in range(1, W+2):
        if N == 1:
            dp[1][tree][move] = max(dp[1][tree-1][move] + 1, dp[2][tree-1][move-1] + 1)
            dp[2][tree][move] = max(dp[1][tree-1][move-1], dp[2][tree-1][move])
        else:
            if tree == 1 and move == 1:
                continue
            dp[1][tree][move] = max(dp[1][tree - 1][move], dp[2][tree - 1][move-1])
            dp[2][tree][move] = max(dp[1][tree - 1][move - 1]+1, dp[2][tree - 1][move]+1)

print(max(dp[1][T][W + 1], dp[2][T][W + 1]))