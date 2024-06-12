def acm_hotel(h, w, n):
    floor = n % h
    room = n // h + 1
    if floor == 0:
        floor = h
        room -= 1
    return floor * 100 + room

tc = int(input())
for _ in range(tc):
    h, w, n = map(int, input().split())
    print(acm_hotel(h, w, n))