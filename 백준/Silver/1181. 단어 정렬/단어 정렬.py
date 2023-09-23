N = int(input())

text_sort = [0]*N

for idx in range(N):
    text_sort[idx] = input()

text_sort = sorted(set(text_sort), key=lambda x: (len(x), x))

for text in text_sort:
    print(text)