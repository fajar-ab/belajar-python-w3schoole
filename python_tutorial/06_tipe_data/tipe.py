"""
Python memiliki tipe data berikut bawaan secara default, dalam kategori ini:

Jenis Teks      :	str
Jenis Numerik   :	int, float, complex
Jenis Urutan    :	list, tuple, range
Jenis Pemetaan  :	dict
Set Jenis       :	set, frozenset
Tipe Boolean    :	bool
Jenis Biner     :	bytes, bytearray, memoryview
Tidak ada Jenis :	NoneType
"""

# mengatur type data

x = "hello world"
print(x) # display x
print(type(x)) # display the data type of x

x = 20
print(x) # display x
print(type(x)) # display the data type of x

x = 20.5
print(x) # display x
print(type(x)) # display the data type of x

x = 1j
print(x) # display x
print(type(x)) # display the data type of x

x = ["apple", "banana", "cherry"]
print(x) # display x
print(type(x)) # display the data type of x

x = ("apple", "banana", "cherry")
print(x) # display x
print(type(x)) # display the data type of x

x = range(10)
print(x) # display x
print(type(x)) # display the data type of x

x = {"name": "jhon", "age": 36}
print(x) # display x
print(type(x)) # display the data type of x

x = {"apple", "banana", "cherry"}
print(x) # display x
print(type(x)) # display the data type of x

x = frozenset({"apple", "banana", "cherry"})
print(x) # display x
print(type(x)) # display the data type of x

x = True
print(x) # display x
print(type(x)) # display the data type of x

x = b"hello"
print(x) # display x
print(type(x)) # display the data type of x

x = bytearray(5)
print(x) # display x
print(type(x)) # display the data type of x

x = memoryview(bytes(5))
print(x) # display x
print(type(x)) # display the data type of x

x = None
print(x) # display x
print(type(x)) # display the data type of x
