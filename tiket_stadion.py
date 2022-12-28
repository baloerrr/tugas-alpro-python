# Tenny

print("Silahkan Pilih Tribun -\n" \
        "1. Tribun VIP\n" \
        "2. Tribun Timur\n" \
        "3. Tribun Barat\n" \
        "4. Tribun Selatan\n" \
        "5. Tribun Utara\n");

vip = 50000
timur = 30000
barat = 25000
selatan = 20000
utara = 18000
jmlPenonton = int(input("Masukkan Jumlah Penonton: "));
pilihan = input("Pilih Tribun: ");
totalPembayaran = int;

# match pilihan:
#     case "1": 
#         totalPembayaran = vip * jmlPenonton;
#         print("Harganya: ", totalPembayaran);
#     case "2": 
#         totalPembayaran = timur * jmlPenonton;
#         print("Harganya: ", totalPembayaran);
#     case "3": 
#         totalPembayaran = barat * jmlPenonton;
#         print("Harganya: ", totalPembayaran);
#     case "4": 
#         totalPembayaran = selatan * jmlPenonton;
#         print("Harganya: ", totalPembayaran);
#     case "5": 
#         totalPembayaran = utara * jmlPenonton;
#         print("Harganya: ", totalPembayaran);
#     case _:
#         print("Tribun tidak ada");


if pilihan == "1":
    totalPembayaran = vip * jmlPenonton;
    print("Harganya: ", totalPembayaran);
elif pilihan == "2":
    totalPembayaran = timur * jmlPenonton;
    print("Harganya: ", totalPembayaran);
elif pilihan == "3":
    totalPembayaran = barat * jmlPenonton;
    print("Harganya: ", totalPembayaran);
elif pilihan == "4":
    totalPembayaran = selatan * jmlPenonton;
    print("Harganya: ", totalPembayaran);
elif pilihan == "5":
    totalPembayaran = utara * jmlPenonton;
    print("Harganya: ", totalPembayaran);
else:
    print("there isn't")