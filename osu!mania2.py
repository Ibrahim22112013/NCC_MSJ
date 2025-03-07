x=int(input())
n=[]
for i in range(x):
    y=int(input())
    m=[]
    for j in range(y):
        z=input()
        l=z.index('#')+1
        m.append(str(l))
    m=m[::-1]
    n.append(m)   
for i in n:
    print(' '.join(i))    