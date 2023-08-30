for test_case in range(int(input())):
    R, S = input().split()
    R = int(R)

    for el in S:
        print(el*R, end='')
    print()
