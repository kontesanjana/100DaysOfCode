n = int(input("enter the number:"))
for i in range(2,n):
    if n % i == 0:
        print("not a prime number")
        break
else:
    print("prime number")

