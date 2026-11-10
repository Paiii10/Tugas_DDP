# #nomor 1
def celcius_ke_fahrenheit(celcius):
    hasil = (celcius * (9 / 5)) + 32
    print(hasil)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print("----------------------------------------------------")
#nomor2
def is_genap(bilangan):
    return bilangan % 2 == 0

print(is_genap(4))
print(is_genap(7))

print("----------------------------------------------------")
#nomor3
def nilai(skor):
    if skor >= 80:
        return "lulus"
    elif skor <= 60:
        return "gagal"
    else:
        return "nilai kamu pas pasan"

print(nilai(80))
print(nilai(70))
print(nilai(60))

print("----------------------------------------------------")
#nomor4
def bilangan(angka):
    for i in range(1, angka+1):
        if i % 2 != 0:
            print(i, end=",")

bilangan(20)