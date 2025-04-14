x=int(input())
y=input()
one=y.count('n')
zero=y.count('z')
z=["0"]*zero
o=["1"]*one
s=o+z
print(' '.join(s))