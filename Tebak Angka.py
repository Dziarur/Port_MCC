import random

tebak_angka = random.randint(1,30)
print("Game Tebak Angka")
print("Saya mempunyai angka dari 1-30")

while(True):
    jawaban = int(input("Masukkan Tebakan Anda = "))
    if jawaban == tebak_angka:
        print("Selamat, jawaban anda benar")
        break
    else:
        print("Ayo Coba Lagi")
        pilih = input("Apakah Nyerah (y/n) = ")
        if pilih == "y":
            print(f"angkanya adalah = {tebak_angka}")