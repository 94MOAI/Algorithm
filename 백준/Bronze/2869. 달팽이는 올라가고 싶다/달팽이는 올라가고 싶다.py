A, B, V = map(int, input().split())

# A + (A-B)*day >= V
# day >= (V-A) / (A-B)

if (V-A)%(A-B) == 0:
    print(int((V-A)/(A-B))+1)
else:
    print(int((V-A)/(A-B))+2)

