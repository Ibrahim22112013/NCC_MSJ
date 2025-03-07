x = int(input())  
y = list(map(int, input().split()))  
h = sum(y)  
l = []  
 
for i in range(x):  
    s = h - y[i]  
    n = x - 1  
    
    if s % n == 0 and s // n == y[i]:  
        l.append(i + 1)  
 
print(len(l))  
if l:  
    print(*l)