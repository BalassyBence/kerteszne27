#8. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a
#képernyőre eddig a számig, egymástól szóközzel elválasztva!
n = int(input("szam"))
for i in range(1,n+1):
    print(i,end=" ")