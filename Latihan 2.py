#input nilai variable
a=input ("masukan nilai a:")
b=input ("masukan nilai b:")

#cetak nilai variable
print("variable a=",a)
print("variable b=",b)

#cetak hasil operasi kedua variable dengan string format
print("hasil penggabungan {1}&{0}=%s".format(a,b)%(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil penjumlahan {1}+{0}=%s".format(a,b)%(a+b))
print("hasil pembagian {0}/{1}=%s".format(a,b)%(a/b))
