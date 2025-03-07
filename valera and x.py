x=int(input())
h=[]
m=''
for i in range(x):
    y=input()
    l=[]
    l.extend(y)
    h.append(l)
    if len(set(y))!=2:
        m='NO'
s=0
n=h[0][0]  
if x%2!=0 and m!='NO':
    for i in range(int(x/2)):
        if h[i][i]==h[i][(x-1)-s]: 
            m='YES'
        else:
            m='NO'
            break
        h[i].remove(h[i][i])   
        h[i].remove(h[i][(x-1)-s-1])
        s+=1
if m=='YES':      
    if h[int(x/2)][int(x/2)]==n:
         m='YES'
         h[int(x/2)].remove(h[int(x/2)][int(x/2)])
    else :
         m='NO' 
    s=int(x/2)-1 
    i=0
    o=int(x/2)+1
    if m=='YES':
        for j in range(int(x/2)+1,x):
              if h[j][s]==h[j][o+i]: 
                   m='YES'
              else:
                   m='NO'
                   break
              h[j].remove(h[j][s])   
              h[j].remove(h[j][o+i-1])
              i+=1    
              s-=1
        k=[]          
        for i in h:
              if len(set(i))==1 and n not in i :
                   m='YES'  
                   k.append(i[0])
              else:
                   m='NO'  
                   break
        if len(set(k))==1 and m=='YES':
              m='YES'  
        else:
            m='NO'    
print(m)             