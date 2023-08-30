alphabet = [-1 for _ in range(ord('z')-ord('a')+1)]

text = input()

for idx in range(len(text)):
    text_idx = ord(text[idx])%ord('a')
    if alphabet[text_idx] == -1:
        alphabet[text_idx] = idx

print(*alphabet)