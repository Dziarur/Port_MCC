import random

tebak_angka = random.randint(1,30)
print(tebak_angka)
print("Game Tebak Angka")
print("Saya mempunyai angka dari 1-30")

while(True):
    jawaban = int(input("Masukkan Tebakan Anda = "))
    if jawaban == tebak_angka:
        print("Selamat, jawaban anda benar")
        break
    else:
        print("Ayo Coba Lagi")