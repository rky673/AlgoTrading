p = 6500
ir = 30
c = 1200
t = 24
for _ in range(1, t + 1):
    if _ == 12:
        p = p - 500
    p = p + ir * p / 100 - c
    print(int(p))
