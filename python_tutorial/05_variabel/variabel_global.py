# variabel global
# dapat digunakan baik di dalam fungsi dan di luar

# x = "awesome"

# def my_func():
#     print("python is", x)

# my_func()


# contoh 

# x = "awesome"

# def my_func():
#     x = "fantastic"
#     print("python is", x)

# my_func()

# print("python is", x)

# kata kunci global

x = "awesome"

def my_func():
    global x
    x = "fantastic"

my_func()

print("python is", x)
