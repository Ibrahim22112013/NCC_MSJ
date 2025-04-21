x=int(input())
for i in range(int(x)):
    h=int(input())
    k=[]
    l=input()
    k.extend(l)
    right=-1
    left=0
    for j in range(int(len(k)/2)):
        if (k[right]=="0" and  k[left]=="1") or (k[right]=="1" and  k[left]=="0"):
           k.pop(-1) 
           k.pop(0)
        else:
            break
    print(len(k))           