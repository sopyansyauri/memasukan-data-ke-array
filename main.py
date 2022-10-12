# PROGRAM MEMASUKAN DATA NAMA MAHASISWA KE ARRAY/LIST


angka = []



c = True

while(c):
    masukan = str(input("masukan Nama: "))
    angka.append(masukan)
    data = input("apakah mau di tambah yes/no: ")
    if (data == "yes"):
        c = True
    elif (data == "no"):
        c = False
    else:
        break

jumlah = range(len(angka))
# print(type(jumlah))

pilih = input("Apakah data nya mau dilihat yes/no: ")
if (pilih == "yes"):
    print("\n")
    print("LIST DATA NAMA MAHASISWA")
    for i in jumlah:
        print(f"{i+1}. {angka[i]}")
elif (pilih == "no"):
    print("Terimakasih banyak")


# print(angka[0])
