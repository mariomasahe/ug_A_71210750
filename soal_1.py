a = int(input("masuukan awal deret:"))
b = int(input("masukan akhir deret:"))

for i in range(a,b):
        if i%6 != 6 and i%3 != 0 and i%2 != 0 :
            print(i,end=' ')
