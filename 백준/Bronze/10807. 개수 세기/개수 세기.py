N = int(input())

numbers = list(map(int, input().split()))
target = int(input())

answer = 0

for number in numbers:
    if number == target:
        answer += 1

print(answer)