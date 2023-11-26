import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
two_point = [0]
total = 0

for i in range(N):
  total += arr[i]
  two_point.append(total)


for i in range(M):
  a, b = map(int, input().split())
  print(two_point[b] - two_point[a - 1])