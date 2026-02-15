import random
import time

TARGET_SIZE = 50_000
MAX_NUMBER = 200_000

# -----------------------
# LIST VERSION
# -----------------------
start = time.perf_counter()

numbers_list = []

while len(numbers_list) < TARGET_SIZE:
    n = random.randint(1, MAX_NUMBER)
    if n not in numbers_list:
        numbers_list.append(n)

end = time.perf_counter()
list_time = end - start

print(f"List time: {list_time:.4f} seconds")


# -----------------------
# SET VERSION
# -----------------------
start = time.perf_counter()

numbers_set = set()

while len(numbers_set) < TARGET_SIZE:
    n = random.randint(1, MAX_NUMBER)
    numbers_set.add(n)   # duplicates ignored automatically

end = time.perf_counter()
set_time = end - start

print(f"Set time: {set_time:.4f} seconds")

print("\nSpeed comparison:")
print(f"Set is about {list_time / set_time:.2f}x faster")
