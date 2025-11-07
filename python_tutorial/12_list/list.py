# list digunakan untuk meyimpan beberapa item dalam satu variabel
# list dibuat dengan menggunakan tanda kurung siku

this_list = ["apple", "banana", "cherry"]
print(this_list)

# item list diurutkan, dapat diubah dan memungkinkan nilai duplikat
# item pertama memiliki index [0], item kedua memiliki index [1] etc

# list dapat memiliki item dengan nilai duplikat
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)

# untuk melihat berapa banyak item dalam list
print(len(this_list))

# item list dapat berupa tipe data apapun
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 9, 7, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# sebuah list dapat berisi tipe data yang berbeda
list1 = ["abc", 123, True, 40.3, "male"]

print(list1)

# list didefinisikan sebagai object dengan type data 'list'
print(type(list1))

# dimungkinkan juga untuk menggunakan 'list()' kontruktor sebuah daftar
this_list = list(("apple", "banana", "cherry")) 

print(this_list)