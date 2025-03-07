x=int(input())
n=[]
for i in range(x):
    y=input()
    if len(y)>10:
        n.append(y[0]+str(len(y)-2)+y[-1])
    else:
        n.append(y)    
for i in n:
    print(i)        