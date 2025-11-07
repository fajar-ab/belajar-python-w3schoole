# access list items

# item list diindex dan anda dapat mengaksesnya dengan mengacu
# pada nomor index
this_list = ["apple", "banana", "cherry"]
print(this_list[1])

# pengindeksan negatif dimulai dari belakang
print(this_list[-1])

# menentukan tentang index dengan menentukan dimana untuk memulai 
# dan dimana untuk mengakhiri jangkauwan. saat menentukan rentang
# nilai kembalian akan menjadi list baru
this_list = ["apple", "banana", "cherry", "orange","kiwi", "melon", "mango"]

print(this_list[2:5])

print(this_list[:4])
# akan mengembalikan item dari index 0 ke index 4

print(this_list[2:])
# akan mengembalikan item dari index 2 ke akhir

print(this_list[-4:-1])
# mengembalikan item dari 'orange' index -4, tapi tiak termasuk 'manggo' index -1

# periksa apakah 'apple' ada dalam list
print("apple" in this_list)