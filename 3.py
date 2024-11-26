#3. Készítsünk programot, amely kiszámolja az első 100 db páros szám összegét 
n=200
osszeg = 0
counter = 0
for i in range(1, n+1, 2):
    osszeg += i
    counter += 1
    print(osszeg , counter)