totalPembayaran = int;
jmlPenumpang = int(input("Masukkan Jumlah Penumpang: "));
usia = int(input("Masukkan Usia: "));

if usia > 10:
    totalPembayaran = 50000 * jmlPenumpang;
    print("Total Pembayaran: ", totalPembayaran);
else:
    totalPembayaran = 25000 * jmlPenumpang;
    print("Total Pembayaran: ", totalPembayaran)
