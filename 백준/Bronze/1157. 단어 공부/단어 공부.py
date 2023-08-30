text = input().upper()

D = dict()

for char in text:
    if D.get(char):
        D[char] += 1
    else:
        D[char] = 1

mx = 0
alphabet = ''
condition = True

for key, value in D.items():
    if mx < value:
        mx = value
        condition = True
        alphabet = key
    elif mx == value:
        condition = False

if condition:
    print(alphabet)
else:
    print('?')