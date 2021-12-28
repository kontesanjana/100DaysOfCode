n = int(input())
m = n+1
for i in range(1,m):
    k = m-i
    print("# " * k)

#or - another method

a = int(input())
for i in range(a):
    for j in range(a-i):
        print("# ", end="")
    print()
