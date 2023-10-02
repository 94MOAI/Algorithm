while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break
    elif A < B and B%A==0:
        print('factor')
    elif A > B and A%B==0:
        print('multiple')
    else: # 첫번째 숫자가 두번째 숫자의 약수와 배수 모두 아닌 경우
        print('neither')