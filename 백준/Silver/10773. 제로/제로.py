numbers = []
for _ in range(int(input())):
    N = int(input())
    if not N:
        numbers.pop()
    else:
        numbers.append(N)

print(sum(numbers))