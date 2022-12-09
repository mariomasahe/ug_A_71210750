a = int(input("masukan pembatas:"))
b = int(input("masukan angka yang dilaranag:"))

for i in range(0,a,1):
    if i == b:
        continue
    print(i,end='')
