x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# mengembalikan True karna x sama object dengan z

print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)


# is    - memeriksa apakah kedua variabel menujuk ke object yang sama dalam memory
# ==    - memeriksa apakah nilai dari kedua variabel sama

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)