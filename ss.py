#első 100 természetes szám összege
"""db=0
for i in range(0,101):
    db += i
print(db)


#összeszorozza az első 7 számot
db=1
for i in range(1,8):
    db *= i
print(db)
"""

db=0
e=0
for i in range(0,1000):
    if i %2==0:
       db += i
       e += 1
if e == 100:
    print(db)


db=0
for i in range(0,101):
    if i %2==1:
       db += i
print(db)

for i in range(1,21):
    if i %2==0:
        print(f"páros:",i)
    elif i %2==1:
        print(f"páratlan:",i)

n = int(input("szám:"))
db=0
for i in range(1,n+1):
    db += i
print("összeg:",db)
db = db/n
print("átlag",db)

a=int(input("szám egy:"))
b=int(input("szám kettő:"))
db=0
valtozo=0
for i in range(a,b+1):
    db += i
    valtozo += 1
print("összeg:",db)
db=db/valtozo
print("átlag",db)

n = int(input("szám:"))
for i in range(1,n+1):
    print(i, end=" ")
