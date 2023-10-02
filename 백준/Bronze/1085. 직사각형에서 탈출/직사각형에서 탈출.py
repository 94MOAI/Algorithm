X, Y, W, H = map(int, input().split())

result = [X-0, Y-0, W-X, H-Y]

print(min(result))