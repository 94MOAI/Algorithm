total = set(i for i in range(1, 30+1))

students = set(int(input()) for _ in range(28))

answer = list(total - students)
answer.sort()
[print(el) for el in answer]


