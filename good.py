x=int(input())
matrix=[]
for i in range(x):
    y=list(map(int,input().split()))
    matrix.append(y)
for i in range(2):
    if i==0:
        row=0
        col=0
        row1=0
        col1=1
        diag=[]
        sec1diag=[]
        sec2diag=[]
        for j in range(len(matrix)):
            diag.append(matrix[row][col])
            if j <len(matrix)-1:  
                sec1diag.append(matrix[row1][col1])
                sec2diag.append(matrix[col1][row1])
            col+=1
            row+=1
            row1+=1
            col1+=1
    else:
        col=len(matrix)-1
        row=0
        row1=0
        col1=col-1
        diaG=[]
        sec3diag=[]
        sec4diag=[]
        for j in range(len(matrix)):
            diaG.append(matrix[row][col])
            if j <len(matrix)-1:  
                sec3diag.append(matrix[row1][col1])
                sec4diag.append(matrix[col1][row1])
            col-=1
            row+=1
            row1+=1
            col1-=1
mid2=[]
m=int(len(matrix)/2)+1
mid=matrix[m]
for i in range(x):
     mid1=matrix[i][m]
     mid2.append(mid1)
print (mid)
print( diag)
print(sec1diag)
print(sec2diag)
print(sec3diag)
print(sec4diag)
print(diaG)
print( mid2)
 
