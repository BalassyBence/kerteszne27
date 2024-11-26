#4. Készítsünk programot, amely kiszámolja az első 100 db páratlan szám összegét
n = 200
db = 1
for i in range(1, n+1, 2):
    db += i
    print(i)