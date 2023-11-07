N = int(input())
number = 0
answer = 0
while True:
    number += 1
    if number**2 <= N:
        answer +=1
        continue
    else:
        break

print(answer)