print("======= Program Manipulasi String =======\nPilihan Menu :\n1. Hitung Kata\n2. Ubah Kata\n")

angka = int(input("Pilihan anda : "))
kalimat = input("Masukkan sebuah kalimat/kata : ")

if angka == 1:
    kata = input("Masukkan kata yang ingin dihitung :")

    def pilihan_1(kalimat, kata):
        hitung_kata = kalimat.count(kata)
        return hitung_kata

    hasil_pilihan1 = pilihan_1(kalimat, kata)
    print("Terdapat sebanyak ", hasil_pilihan1, " kata", kata, " di dalam kalimat")

elif angka == 2:
    ubah_kata = input("Masukkan kata yang ingin diubah : ")
    pengganti_kata = input("Masukkan kata pengganti : ")

    def pilihan_2(kalimat, ubah_kata, pengganti_kata):
        hasil_ubah = kalimat.replace(ubah_kata, pengganti_kata)
        return hasil_ubah

    hasil_pilihan2 = pilihan_2(kalimat, ubah_kata, pengganti_kata)
    print("String berhasil diubah menjadi : ", hasil_pilihan2)

else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")