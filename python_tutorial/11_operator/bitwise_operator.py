a = 6
b = 3


"""
operator & membandingkan setiap bit dan mengatur menjadi 1
jika kedua bit tersebut adalah 1, selain itu akan diatur menjadi 0
"""
hasil = a & b

print(f"{a} = {a:016b}")
print(f"{b} = {b:016b}")
print("-" * 20)
print(f"{hasil} = {hasil:016b}\n")


"""
operator | membandingkan setiap bit dan menangaturnya menjai 1
jika salah sat atau keduanya adalah 1, jika tidak maka 0
"""
hasil = a | b

print(f"{a} = {a:016b}")
print(f"{b} = {b:016b}")
print("-" * 20)
print(f"{hasil} = {hasil:016b}\n")


"""
operator ^ membandingkan setiap bit dan mengaturnya menjadi 1
jika hanya satu yang 1, jika tidak maka diatur 0
"""
hasil = a ^ b

print(f"{a} = {a:04b}")
print(f"{b} = {b:04b}")
print("-" * 8)
print(f"{hasil} = {hasil:04b}\n")


"""
operator ~ membalik setiap bit (0 mejadi 1 dan 1 menjadi 0)
"""
hasil = ~b

print("membalikkan 3 menjadi -4:")
print(f"{b:2} = {b:016b}")
print(f"{hasil} = {format(hasil & 0xFFFF, "016b")}\n") # format biner two complement


a = 3
b = 2

"""
operator << menyisipkan sejumlah 0 (dalam kasus ini 2) dari sisi kanan,
dan membiarkan jumlah bit paling kiri yang sama banyaknya tergeser keluar (terbuang)
"""
hasil = a << b

print("jika anda mendorong 00 masuk dari kiri:")
print(f"{a:2} = {a:016b}")
print("menjadi")
print(f"{hasil} = {hasil:016b}\n")


a = 8
b = 2

"""
operator >> memindahkan setip bit sejumlah posisi yang ditentukan ke kanan,
ruang kosong dari sisi kiri akan diisi dengan 0
"""
hasil = a >> b

print("jika anda memindahkan setip bit 2 kali kekanan, 8 menjadi 2:")
print(f"{a} = {a:016b}")
print("menjadi")
print(f"{hasil} = {hasil:016b}")