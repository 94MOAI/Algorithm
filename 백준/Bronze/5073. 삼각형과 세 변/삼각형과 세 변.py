while True:
    length = list(map(int, input().split()))
    length.sort()

    if sum(length) == 0:
        break

    if length[2] < length[0] + length[1]:
        if length[0] == length[1] == length[2]:
            print('Equilateral')
        elif length[0] == length[1] or length[0] == length[2] or length[1] == length[2]:
            print('Isosceles')
        else: # length[0] != length[1] != length[2]
            print('Scalene')
    else:
        print('Invalid')