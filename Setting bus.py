x=int(input())
for i in range(x):
    b=int(input())
    k=list(map(int,input().split()))
    new=[0]*(max(k)+2)
    new[k[0]]=1
    y="YES"
    for j in range(1,len(k)):
        if new[k[j]-1]==0 and new[k[j]+1]==0:
            y='NO'
            break
        else:
            y='YES'    
            new[k[j]]=1
    print(y)        