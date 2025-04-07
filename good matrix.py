x=int(input())
matrix=[]
for i in range(x):
    y=list(map(int,input().split()))
    matrix.append(y)
row=0
col=0
diag=[]
col1=len(matrix)-1
diaG=[]
mid2=[]
m=int(len(matrix)/2)
mid=matrix[m]
for j in range(len(matrix)):
    diag.append(matrix[row][col])
    diaG.append(matrix[row][col1])
    mid1=matrix[j][m]
    mid2.append(mid1)
    col+=1
    row+=1
    col1-=1
count=sum(mid)+sum(mid2)+sum(diag)+sum(diaG)-(matrix[m][m]*3)
print(count)
    