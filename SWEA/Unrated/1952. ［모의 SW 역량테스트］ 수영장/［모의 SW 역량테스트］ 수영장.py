def f(month, cost):
    global total
    if month >= 12:
        total = min(total, cost)
        return
    if cost > total:
        return
    f(month + 1, cost + M[month] * P[0])
    f(month + 1, cost + P[1])
    f(month + 3, cost + P[2])
    f(month + 12, cost + P[3])


for test_case in range(int(input())):
    P = tuple(map(int, input().split()))
    M = tuple(map(int, input().split()))
    total = 3000*365 + 1
    f(0, 0)
    print(f"#{test_case + 1} {total}")
