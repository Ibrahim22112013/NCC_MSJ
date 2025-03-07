t = int(input())
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    s = 0
    for p in [(a1, a2, b1, b2), (a1, a2, b2, b1), (a2, a1, b1, b2), (a2, a1, b2, b1)]:
        if (p[0] > p[2]) + (p[1] > p[3]) > (p[2] > p[0]) + (p[3] > p[1]):
            s += 1
    print(s)