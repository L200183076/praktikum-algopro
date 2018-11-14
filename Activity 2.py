##Program Akun
##Dibuat oleh Indraswari L200183076

Nama = "Indraswari Wahyu Pertiwi"
print ("Nama =", Nama)
TanggalLahir = "15 Oktober 2000"
print ("Tanggal Lahir =", TanggalLahir)
print ("Nama Singkat =", Nama[:10], Nama[11]+".", Nama[-7]+".")
print ("Username =", Nama[0]+TanggalLahir[:2]+TanggalLahir[-4:])

import random
acak = random.randint(0,1000)
print("Password =",Nama[0:3]+str(acak))