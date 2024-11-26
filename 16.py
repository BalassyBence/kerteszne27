n = int(input("egesz szam"))
oszto=2

while oszto <= n:
    if n%oszto==0:
        print(oszto)
        n/=oszto
    else:
        oszto+=1