coordinate = []
N = int(input())

for _ in range(N):
    coordinate.append(list(map(int, input().split())))

# print(coordinate)

coordinate.sort(key=lambda x: (x[0], x[1]))

for idx in range(N):
    print(*coordinate[idx])