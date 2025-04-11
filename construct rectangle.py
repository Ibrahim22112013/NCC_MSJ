y=int(input())
for i in range(y):
     x=list(map(int,input().split()))
     if len(set(x))==2:
        if x[0]==x[1]:
            if x[2]%2==0:
                print('YES')
            else:
                print('NO')   
        elif x[0]==x[2]:
            if x[1]%2==0:
                print('YES')
            else:
                print('NO')
        else:
            if x[0]%2==0:
                print('YES')
            else:
                print('NO')       
     elif len(set(x))==1:
        if x[0]%2==0:
            print('YES') 
        else:
            print('NO')  
     else:
         Emma=max(x) 
         x.remove(Emma) 
         if Emma-x[0]==x[1] and  Emma-x[1]==x[0]:
             print('YES') 
         else:
             print('NO')                   
                