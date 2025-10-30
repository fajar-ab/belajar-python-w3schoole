

class MyClass():
    def __len__(self):
        return 0

my_object = MyClass()
print(bool(my_object))


# fungsi dapat mengembalikan boolean

def myFunction():
    return True

print(myFunction())

if myFunction():
    print("yes!")
else:
    print("no!")

# periksa apakah objek dari tipe data tertentu

x = 200
print(isinstance(x, int))