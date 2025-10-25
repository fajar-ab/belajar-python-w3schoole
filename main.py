import time
for i in range(10):
    print(f"\rLoading... {i}", end="")
    time.sleep(1)
print("\nSelesai!")
