alphabet = input()

# 크로아티아 알파벳이 있으면 원래 길이만큼으로 변환!
# dz= 가 z= 보다 앞에 있지 않으면 z=를 우선으로 바꿔버리게 되므로 dz=가 z= 보다 앞에 있어야 한다.
alpha_key = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for alpha in alpha_key:
    if alpha in alphabet:
        # replace는 원본 변환이 일어나지 않는다. 새로운 변수에 할당해야 한다.
        # 길이를 측정하기 위해서 원본에 재할당하는 방식으로 진행
        alphabet = alphabet.replace(alpha, '_')

alphabet_len = 0
for char in alphabet:
    alphabet_len += 1

print(alphabet_len)
