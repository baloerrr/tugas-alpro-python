# Calculator Sederhana Python
# loop = "yes"
# # Mulai
# while loop.lower() == "yes":
#     print("Please select operation -\n" \
#             "- Penjumlahan\n" \
#             "- Pengurangan\n" \
#             "- Perkalian\n" \
#             "- Pembagian\n");

#     # Deklarasi Variabel
#     operation = input("Silahkan Pilih Operasi: ").lower();
#     num1 = float(input("Masukkan nilai pertama: "));
#     num2 = float(input("Masukkan nilai kedua: "));
#     hasil = float;

#     # Proses 
#     match operation:
#             case "penjumlahan":
#                 hasil = num1 + num2;
#                 print("Hasil Penjumlahan: ", hasil);
#             case "pengurangan":
#                 hasil = num1 - num2;
#                 print("Hasil Penjumlahan: ", hasil);
#             case "perkalian":
#                 hasil = num1 * num2;
#                 print("Hasil Penjumlahan: ", hasil);
#             case "pembagian":
#                 hasil = num1 / num2;
#                 print("Hasil Penjumlahan: ", hasil);
#             case _:
#                 print("Maaf operasi yg anda pilih belum tersedia");

         

def calculator():
   loop = "ya"

   while loop.lower() == "ya":
      print("Pilih Operasi\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian")

      choice = input("Pilih Operasi(1/2/3/4):")

      num1 = float(input("Masukkan Nilai Pertama: "))
      num2 = float(input("Masukkan Nilai Kedua: "))
      result = float;

      if choice == '1':
         result = num1 + num2;
         print("Hasilnya Adalah: ", result);

      elif choice == '2':
         result = num1 - num2;
         print("Hasilnya Adalah: ", result);
      elif choice == '3':
         result = num1 * num2;
         print("Hasilnya Adalah: ", result);
      elif choice == '4':
         result = num1 / num2;
         print("Hasilnya Adalah: ", result);
      else:
         print("Invalid input")
      loop = input("Continue?ya/tidak: ");
      if loop == "n":
         break

calculator()
