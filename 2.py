#2. Készítsünk programot, amely kiszámolja az első 7 db természetes szám szorzatát egy ciklus segítségével. 
n = 7
db=1
for i in range(1,n+1):
    db *= i
print(db)