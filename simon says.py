x=int(input())
for i in range(x):
    y=input().split()
    if 'Simon'==y[0] and  'says'==y[1]:
        y.remove(y[0])
        y.remove(y[0])
        print(' '.join(y))