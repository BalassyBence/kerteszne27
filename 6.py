#6. Számítsd ki a felhasználó által bevitt n szám átlagát
n = int(input("egesz szam"))
db=0
while n > 0:
    n -= 1
    db += n
print(db)
