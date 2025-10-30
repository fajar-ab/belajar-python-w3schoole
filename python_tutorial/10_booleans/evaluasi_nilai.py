# evaluasi string dan angka

print(bool("hello"))
print(bool(15))

# evaluasi dua variabel

x = "hello"
y = 15

print(bool(x))
print(bool(y))


# kebanyakan nilai adalah benar

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# beberapa nilai adalah salah

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))