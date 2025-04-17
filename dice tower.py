x=int(input())
h=int(input())
for i in range(x):
    s,g=map(int,input().split())
    if h+s==7 or h+g==7 or h==s or h==g:
        print("NO")
        break
else:
    print("YES")        