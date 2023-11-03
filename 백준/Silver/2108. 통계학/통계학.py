import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr) / len(arr)))
print(arr[len(arr) // 2])


d = dict()
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

mx = max(d.values())
most = []

for i in d:
    if mx == d[i]:
        most.append(i)

if len(most) > 1:
    print(most[1])
else:
    print(most[0])

print(max(arr) - min(arr))