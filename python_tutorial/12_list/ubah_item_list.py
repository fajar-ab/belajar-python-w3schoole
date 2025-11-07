# untuk mengubah nilai dalam item tertentu, lihat indeksnya
this_list = ["apple", "banana", "cherry"]

this_list[1] = "blackcurrant"
print(this_list)

# mengubah nilai item dalam rentang tertentu, tentukan list dengan nilai baru
# dan tunjuk kerentang angka di indeks tempat menyisipkan nilai baru 
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "maggo"]

this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

# ubah nilai kedua dengan menggantinya dengan nilai baru
this_list = ["apple", "banana", "cherry"]

this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)

# ubah nilai kedua dan ketiga dengan menggantinya menjadi satu nilai
this_list = ["apple", "banana", "cherry"]

this_list[1:3] = ["watermelon"]
print(this_list)

# metode menyisipkan item pada index yang ditentukan
this_list = ["apple", "banana", "cherry"]

this_list.insert(2, "watermelon")
print(this_list)