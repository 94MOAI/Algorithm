graph = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for row in range(y, y+10):
        for col in range(x, x+10):
            graph[row][col] = 1

area = 0
for y in range(100):
    for x in range(100):
        if graph[y][x]:
            area += 1

print(area)