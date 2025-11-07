# prioritas operator menjelaskan urutan operasi yang dilakukan

print((6 + 3) - (6 + 3))
"""
() tanda kurung memiliki prioritas tertinggi, dan perlu dievaluasi
terlebih dahulu
perhitungan di atas berbunyi 9 - 9 = 0
"""

print(100 - 3 ** 3)
"""
** exponensial memiliki prioritas lebih tinggi daripada pengurangan,
dan perlu dievaluasi terlebih dahulu
perhitungan di atas berbunyi 100 - 27 = 73
"""

print(100 + ~3)
"""
+x  -x  ~x      Unary plus, unary minus, and bitwise NOT
memiliki prioritas lebih tinggi daripada penambahan,
dan perlu dievaluasi terlebih dahulu
perhitungan di atas berbunyi 100 - 4 = 96
"""

print(100 + 5 * 3)
"""
*  /  //  %     Multiplication, division, floor division, and modulus
memiliki prioritas yang lebih tinggi dari pada penjumlahan,
dan perlu dievaluasi terlebih dahulu
perhitungan diatas berbunyi 100 + 15 = 115s
"""

print(100 - 5 * 3)
"""
+  -            Addition and subtraction
memiliki prioritas yang lebih rendah dari pada perkalian dan 
kita perlu menghitung perkaliannya terlebih dahulu
perhitungan diatas berbunyi 100 - 15 = 85
"""

print(8 >> 4 - 2)
"""
<<  >>          Bitwise left and right shifts
memiliki prioritas lebih rendah dari pada pengurangan, dan kita 
perlu menghitung penguranganya terlebih dahulu.
perhitungan di atas berbunyi 8 >> 2 = 2
"""

print(6 & 2 + 1)
"""
Bitwise AND 
memiliki prioritas lebih rendah dari pada penjumlahan, dan kita 
perlu menggitung penjumlahannya terlebih dahulu.
perhitungan di atas berbunyi 6 & 3 = 2
"""

print(6 ^ 2 + 1)
"""
Bitwise XOR
memiliki prioritas lebih rendah dari pada penjumlahan, dan kita 
perlu menghitung penjumlahannya terlebih dahulu.
perhitungan di atas berbunyi 6 ^ 3 = 5
"""

print(6 | 2 + 1)
"""
Bitwise OR
memiliki prioritas lebih rendah dari pada penjumlahan, dan kita 
perlu menghitung penjumlahannya terlebih dahulu.
perhitungan di atas berbunyi 6 | 3 = 7
"""

print(5 == 4 + 1)
"""
Comparisons, identity, and membership operators
memiliki prioritas lebih rendah dari pada penjumlahan, dan kita 
perlu  menghitung penjumlahanya terlebih dahulu.
perhitungan di atas berbunyi 5 == 5 = True
"""

print(not 5 == 5)
"""
Logical NOT
memiliki priofitas yang lebih rendah dari pada perbandingan "like",
dan kita perlu menghitung perbandingannya terlebih dahulu.
perhitungan di atas berbunyi not True = False
"""

print(1 or 2 and 3)
"""
AND memiliki prioritas yang lebih tinggi dari pada 'or', dan kita 
perlu menghitung ekspresi 'and' terlebih dahulu.
perhitungan di atas berbunyi 1 or 3 = 1
"""

print(4 or 5 + 10 or 8)
"""
OR memiliki prioritas yang lebih rendah dari pada penjumlahan, dan
kita perlu menghitung penjumlahannya terlebih dahulu.
perhitungan di atas berbunyi 4 or 15 or 8 = 4
"""