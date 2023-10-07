import sys
input = sys.stdin.readline

users = []

N = int(input())
for _ in range(N):
    age, name = input().split()
    age = int(age)
    users.append((age, name))

users.sort(key=lambda x:x[0])

[print(*users[idx]) for idx in range(N)]