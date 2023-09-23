'''
x+1 부터 n개 숫자의 합
= n//2*(x+1+x+n)
sum = nx + (n//2)*(n+1)
nx = sum - (n//2)*(n+1)
'''

N, L = map(int, input().split())

for i in range(L, 100+1):
    x = N - i * (i+1) // 2

    if x % i == 0:
        x //= i

        if x + 1 >= 0:
            print(*[i for i in range(x+1, x+i+1)])
            break
else:
    print(-1)