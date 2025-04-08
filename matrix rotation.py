def rot(x):
    x[0][0],x[0][1],x[1][0],x[1][1]=x[1][0],x[0][0],x[1][1],x[0][1]
    return x
l=int(input())
for i in range(l):
    x=[]
    y=list(map(int,input().split()))
    s=list(map(int,input().split()))
    x.append(y)
    x.append(s)
    if x[0][0]<x[0][1] and x[1][0]<x[1][1] and x[0][0]<x[1][0] and x[0][1]<x[1][1]:
        o="Yes"
    else:
        for i in range(3):
            x=rot(x)
            if x[0][0]<x[0][1] and x[1][0]<x[1][1] and x[0][0]<x[1][0] and x[0][1]<x[1][1]:
                   o="Yes"
                   break
            else:
                o="NO"
    print(o)                   
                    
    