#5. Írja ki az első 20 számból a) párosakat b) páratlanokat
n=20
for i in range(1,n+1):
    if i % 2 == 0:
        print("paros",i)
    elif i %2 == 1:
        print("paratlan" ,i)