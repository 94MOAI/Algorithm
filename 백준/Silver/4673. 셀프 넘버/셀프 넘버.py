numbers = set(range(1, 10_000+1))
remove_numbers = set()

for number in numbers:
    for bit in str(number):
        number += int(bit)
    remove_numbers.add(number)

self_numbers = numbers - remove_numbers

# set 정렬!
for number in sorted(self_numbers):
    print(number)
