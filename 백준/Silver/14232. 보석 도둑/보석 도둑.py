N = int(input())
arr = []

for i in range(2, int(N ** 0.5)+1):
    while N % i == 0:
        arr.append(i)
        N //= i

if N != 1:
    arr.append(N)

print(len(arr))
print(*arr)