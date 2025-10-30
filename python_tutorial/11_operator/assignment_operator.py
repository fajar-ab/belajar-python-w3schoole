# operator penugasan digunakan untuk menetapkan nilai 
# kevariabel

x = 5

print(x)

x += 5
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

print("*******")

x = 5
y = 3

print(f"{x} : {x:04b}")
print(f"{y} : {y:04b}")
print("-------- and")
x &= y
print(f"{x} : {x:04b}")


print("*******")

x = 5
y = 3

print(f"{x} : {x:04b}")
print(f"{y} : {y:04b}")
print("-------- or")
x |= y
print(f"{x} : {x:04b}")


print("*******")

x = 5
y = 3

print(f"{x} : {x:04b}")
print(f"{y} : {y:04b}")
print("-------- xor")
x ^= y
print(f"{x} : {x:04b}")

print("*******")

x = 5
y = 3

print(f"{x} : {x:04b} -> {y}")
print("-------- bitwise right shift")
x >>= y
print(f"{x} : {x:04b}")

print("*******")

x = 5
y = 3

print(f"{x} : {x:04b} <- {y}")
print("-------- bitwise left shift")
x <<= y
print(f"{x} : {x:04b}")

print("//////////////////")

# Walrus Operator

numbers = [1,2,3,4,5]

count = len(numbers)
if count > 3:
    print(f"list has {count} elements")

if (count := len(numbers)) > 3:
    print(f"list has {count} elements")

