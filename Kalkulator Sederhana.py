def tambah(a,b):
    return a + b

def kurang (a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    if b == 0:
        print("Tidak bisa membagi dengan 0")
        return 
    else:
        return a / b
    
def pangkat(a,b):
    if b == 0:
        return 1
    else:
        return a ** b

def faktorial(n):
    if n == 0:
        return 1
    else:
        hasil = 1
        for i in range(1, n+1):
            hasil *= i
        return hasil


while(True):
    print(10*"=","KALKULATOR SEDERHANA",10*"=")
    print("Pilih Operasi")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    print("6. Faktorial")

    operasi = input("Pilih Operasi (1-6) = ")
    if operasi in ["1","2","3","4","5"]:
        a = float(input("Masukkan angka pertama = "))
        b = float(input("Masukkan angka kedua = "))
   

    if operasi == "1":
        print("Hasil = ", tambah(a,b))
    elif operasi == "2":
        print("Hasil = ", kurang(a,b))
    elif operasi == "3":
        print("Hasil = ", kali(a,b))
    elif operasi == "4":
        print("Hasil = ", bagi(a,b))
    elif operasi == "5":
        print("Hasil = ", pangkat(a,b))
    elif operasi == "6":
        n = int(input("Masukkan angka = "))
        print("Hasil = ", faktorial(n))
    else:
        print("Error")

    lanjut = input("Apakah ingin lanjut(y/n) = ")
    if lanjut == "n":
        break


