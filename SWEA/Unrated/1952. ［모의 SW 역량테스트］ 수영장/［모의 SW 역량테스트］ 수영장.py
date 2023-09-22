def f(month, amount):
    global total
    if month >= 12:
        total = min(total, amount)
        return
    if amount > total:
        return
    f(month + 1, amount + M[month] * cost[0])
    f(month + 1, amount + cost[1])
    f(month + 3, amount + cost[2])
    f(month + 12, amount + cost[3])


for test_case in range(int(input())):
    cost = tuple(map(int, input().split()))
    M = tuple(map(int, input().split()))
    total = 3000*365 + 1
    f(0, 0)
    print(f"#{test_case + 1} {total}")
