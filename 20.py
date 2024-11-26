n = int(input("szám: "))
for i in range(1,n+1):
    if n%i==0:
        print("X0"*n)
    else:
        print("0X"*n)