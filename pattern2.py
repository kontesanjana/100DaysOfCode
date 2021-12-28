n = int(input())
m = n+1
for i in range(1,m):
    print('# '* i)

#or - another method
k = int(input())
l = k+1
for i in range(1,l):
    for j in range(i):
        print("# ",end="")
    print()