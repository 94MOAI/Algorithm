# 파이썬의 int 함수는 임의의 진법 수를 10진법으로 변환하는데 사용할 수 있다.
n, b = input().split()
print(int(n, int(b)))