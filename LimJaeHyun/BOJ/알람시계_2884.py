def earlier_alarm(h, m):
    if m >= 45:
        m -= 45
    else:
        m += 15
        if h == 0:
            h = 23
        else:
            h -= 1
    return f'{h} {m}'


H, M = map(int, input().split())
print(earlier_alarm(H, M))
