#15. Írj programot, mely eldönti egy számról, hogy prímszám-e.
n = int(input("szam: "))
osztok=0
for i in range(1, n+1):
    if n % i==0:
        osztok+=1
if osztok==2:
    print("prímszám")
else:
    print("összetett szám")