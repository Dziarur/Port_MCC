import random

tebak_angka = random.randint(1,30)
print("Game Tebak Angka")
print("Saya mempunyai angka dari 1-30")

while(True):
    jawaban = int(input("Masukkan Tebakan Anda = "))
    if jawaban > 30:
        print("Angkanya kan cuma dari 1-30, tebak yang bener dong")
    else:
        if jawaban == tebak_angka:
            print("Selamat, jawaban anda benar")
            break
        else:
            print("Ayo Coba Lagi")
            pilih = input("Apakah Nyerah (y/n) = ")
            if pilih == "y":
                print(f"Jawabannya adalah = {tebak_angka}")
                break   