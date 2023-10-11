import sys
input = sys.stdin.readline

def dungeon(hp, atk):
    cur_hp = hp
    for t, a, h in array:
        if t == 1:
            cnt = h // atk - 1
            if h % atk:
                cnt += 1

            cur_hp = max(cur_hp - (a * cnt), 0)
            if not cur_hp:
                return False
        else:
            atk += a
            cur_hp = min(cur_hp + h, hp)
    return True


N, atk = map(int, input().split())
array = []
dragon_atk = 0
dragon_hp = 0
for _ in range(N):
    t, a, h = map(int, input().split())
    if t == 1:
        dragon_atk = max(a, dragon_atk)
        dragon_hp = max(h, dragon_hp)
    array.append([t, a, h])

start = 1
end = dragon_atk * dragon_hp * N
max_hp = end
while start <= end:
    mid = (start + end) // 2

    if dungeon(mid, atk):
        end = mid - 1
        max_hp = min(max_hp, mid)
    else:
        start = mid + 1
print(max_hp)