N = int(input())

if not N % 4:
    if not N % 100:
        if not N % 400:
            print(1)
        else: # N % 400:
            print(0)
    else: # N % 100:
        print(1)
else:
    print(0)