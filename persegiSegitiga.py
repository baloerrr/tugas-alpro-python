#  Program Luas Persegi dan Segitiga
# Heni Yulia

print("Silahkan Pilih: -\n" \
        "1. Persegi\n" \
        "2. Segitiga\n" \
        );

pilihan = input("Silahkan Pilih: ");
luas = float;

match pilihan:
    case "1":
        # deklarasi variabel persegi
        sisi = float(input('Masukkan sisi: '));
        luas = sisi * sisi;
        print("Hasil luas Persegi: ", luas);

    case "2": 
        # deklarasi variabel segitiga
        alas = float(input('Masukkan alas: '));
        tinggi = float(input('Masukkan tinggi: '));
        luas = (alas * tinggi)/2;
        print("Hasil Luas Segitiga: ", luas);