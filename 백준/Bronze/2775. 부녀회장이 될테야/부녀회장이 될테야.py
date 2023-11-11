# 0 1 2 3
# 1 1 3 6
# 2 1 4 10

for t in range(int(input())):
    k = int(input())
    n = int(input())

    apt = [[0]*(n) for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                apt[i][j] += j + 1
            else:
                apt[i][j] = apt[i-1][j]+apt[i][j-1]

    print(apt[k][n-1])
