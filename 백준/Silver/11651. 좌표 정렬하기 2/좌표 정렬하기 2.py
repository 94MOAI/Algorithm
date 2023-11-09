import sys
input = sys.stdin.readline

coordinate = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    coordinate.append((x, y))

coordinate.sort(key=lambda x :(x[1], x[0]))

[print(*idx) for idx in coordinate]