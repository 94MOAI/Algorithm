N = list(input())

for number in N:
    number = int(number)

N.sort(reverse=True)

print(''.join(map(str, N)))