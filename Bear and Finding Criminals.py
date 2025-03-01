x,y=map(int,input().split())
h=list(map(int,input().split()))
y-=1
m=h[y]
l=y-1
r=y+1
for i in range(x):
    if l>=0 and r<x:
        if h[l]>0 and h[r]>0:
            m+=h[l]+h[r]
    elif l>=0:
        m+=h[l]
    elif r<x:
        m+=h[r] 
    l-=1
    r+=1
print(m)                   