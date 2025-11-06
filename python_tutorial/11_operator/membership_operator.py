# operator keangotaan digunakan untuk menguji 
# jika urutan berada di dalam object

x = ["apple", "banana"]

print("banana" in x)
# mengembalikan True karna urutan dengan nilai 'banana' terdapat dalam list

print("pineaple" not in x)
# mengembalikan True karna urutan dengan nilai 'pineaple' tidak terdapat dalam list

# operator keanggotaan juga berkerja untuk string

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)