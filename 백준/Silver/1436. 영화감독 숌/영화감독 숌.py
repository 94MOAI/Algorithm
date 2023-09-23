# number = 666
# answer = 0
# 
# N = int(input())
# 
# while True:
# 
#     cnt = 0
#     check = str(number)
#     for bit in check:
#         if bit == '6':
#             cnt += 1
#     if cnt >= 3:
#         answer += 1
# 
#     if N == answer:
#         print(number)
#         break
#     else:
#         number += 1

# 6이 아니라 666 포함!

N = int(input())
number = 666

while N:
    if "666" in str(number):
        N -= 1
    number += 1

print(number - 1)