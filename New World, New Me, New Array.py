import math
 
t = int(input())
 
for _ in range(t):
    n, k, p = map(int, input().split())
 
    if k < -n * p or k > n * p:
        print(-1, end=" ")
    else:
        steps = math.ceil(abs(k) / p)
        if steps <= n:
            print(steps, end=" ")
        else:
            print(-1, end=" ")
 
print()