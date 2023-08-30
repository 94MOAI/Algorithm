def QA(lst):
    result = 0
    for el in lst:
        result += el**2
    return result%10


N = list(map(int, input().split()))

print(QA(N))