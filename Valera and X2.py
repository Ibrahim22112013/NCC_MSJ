x=int(input())
new=[]
for i in range(x):
    new1=[]
    y=input()
    new1.extend(y)
    new.append(new1)
col1=0
row1=0 
diag=[]
nondiag=[] 
col2=x-1 
for row in range(x):
        diag.append(new[row1][col1])
        diag.append(new[row1][col2]) 
        for j in range(x):
            if j!=col1 and j!=col2:
               nondiag.append(new[row1][j]) 
        row1+=1
        col1+=1
        col2-=1       
if len(set(diag))==1 and len(set(nondiag))==1 and nondiag[0]!=diag[0]:
    print('YES')
else:
    print('NO')    
   