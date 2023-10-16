def gcd(N, M):
    while M > 0:
        N, M = M, N % M
    return N

def lcm(N, M):
    return N * M // gcd(N, M)


N, M = map(int, input().split())


print(gcd(N, M))
print(lcm(N, M))