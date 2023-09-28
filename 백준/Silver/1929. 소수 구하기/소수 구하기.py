# 일반 소수 알고리즘 -> 88% 실패

# def solution_round(x):
#     if x - int(x) >= 0.5:
#         return x+1
#     else:
#         return x
#
# def prime(M, N):
#     for number in range(M, N+1):
#         condition = False
#         for div in range(2, int(solution_round(number**0.5))+1):
#             if number % div:
#                 condition = True
#                 continue
#             else:
#                 condition = False
#                 break
#         if condition:
#             print(number)
#
# M, N = map(int, input().split())
# prime(M, N)


# 에라토스테네스의 체 변형
M, N = map(int, input().split())

isPrime = [True]*(N+1)
isPrime[1] = False

# 에라토스테네스의 체 원리 적용
for i in range(2, N+1):
    for j in range(2, N+1):
        # 2 ~ N 까지의 숫자를 순회하면서
        # 2 ~ N 까지의 숫자를 곱한 숫자가 N 범위 안에 있으면 False!
        if i*j > N:
            break
        isPrime[i * j] = False

# M, N 까지 순회하면서 True 라면 출력
for idx in range(M,N+1):
    if isPrime[idx]:
        print(idx)