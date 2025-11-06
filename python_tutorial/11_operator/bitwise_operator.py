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
