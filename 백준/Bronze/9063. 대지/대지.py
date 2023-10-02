X = []
Y = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

W = max(X) - min(X)
H = max(Y) - min(Y)

print(W*H)