import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
qty = 0
for i in range(n):
  qty += sum(arr[:i+1])

print(qty)