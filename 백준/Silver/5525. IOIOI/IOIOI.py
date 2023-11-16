import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
l, r = 0, 0
answer = 0

while r < M:
    if S[r:r + 3] == 'IOI':
        r += 2
        if r - l == 2 * N:
            answer += 1
            l += 2
    else:
        l = r = r + 1

print(answer)