kata = input("Masukkan kata : ")
jumlah_huruf = int(len(kata))

def cetakHuruf(kata):
    if jumlah_huruf % 2 == 0 :
        awal = kata[0:3]
        akhir = kata[-3:]
        print("Huruf yang diambil pada kata", kata, " adalah ", awal, " dan ", akhir)
    else:
        bagian = int((jumlah_huruf-3)/2)
        tiga_huruf = kata[bagian:-bagian]
        print("Huruf yang diambil pada kata ", kata, " adalah ", tiga_huruf)
    return

cetakHuruf(kata)