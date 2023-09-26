total = int(input())

# 최대 갯수는 3kg으로만 total의 무게를 만드는 경우
mx_amount = (total//3) +1

answer = []
for i in range(mx_amount):      # 3 kg 의 경우
    for j in range(mx_amount):  # 5 kg 의 경우
        if 3*i + 5*j == total:
            answer.append(i+j)
if answer:
    print(min(answer))
else:
    print(-1)