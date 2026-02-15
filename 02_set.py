
# SET == NO DUPLICATIONS!!!!


# DONT DO  !!
# s0 = { }  --> this will not give you en EMPTY set

# DO
s0 = set()  # for empty set

print(s0)

s1 = {10, 50, 20}
print(s1)
# print(type(s1))
# print(type(5))
# print(type(8.5))
# print(type([1,2,3]))
# print(type('hello'))

s2 = set()
s2.add(8)
s2.add(10)
s2.add(10)
print(s2)

s3 = set( [4, 7, 8, 9, 9, 9] )
print(s3)
# print(s3[0])  # ERROR - does not support random access
print(list(s3)[0])

nums = [5, 2, 1, 9, -4, 2]
print(f"duplication in {nums} ? {len(nums) != len(set(nums))}")

nums = [5, 2, 1, 9, -4, 30]
print(f"duplication in {nums} ? {len(nums) != len(set(nums))}")

s4 = {"Geeks", "python", 10, 52.7, True}
print(s4)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)
# fs.add(1)  # ERROR
print(fs)

s5 = {1, 4, 5, 5, 8}
print(s5)  # 5 will appear 1 time
s5.remove(4) # remove item with value 4 , if item not exist -- ERROR
print('After remove 4: ', s5)

# s5.remove(4)  # ERROR

if 4 in s5:
    s5.remove(4)

s6 = {1, 4, 5, 8}
print(s6)
s6.discard(4)  # remove item with value 4 , if item not exist -- no error
print('Discard 4: ', s6)
s6.discard(4)
print('Discard 4: ', s6)
print(s6.pop())  # will remove + return a random value [sometimes 1st]  -- not common
print(s6)

# del s6[0]  # ERROR

'''
Exercise 1: The "Guest List" Cleaner
You have a list of names for a party, but some people signed up twice.
- Create a list called guests with these values: "Alice", "Bob", "Charlie", "Alice", "David", "Bob"
- Use a set to automatically remove the duplicates
- Check if "Emma" is in your set. If she is not there, add her
- Print the final number of unique guests using len()
'''
names = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
set_names = set(names)
print(set_names)
if 'Emma' not in set_names:
    set_names.add('Emma')
print(f"Number of guests {len(set_names)}")

'''
Exercise 2: Safe Deletion Race
- Create a set called codes containing: 101, 102, 103, 104
- Use .pop() to remove one number and print it (this is not deterministic which item will be removes)
   so it feels like random
- Try to use .remove() to delete the number 999 --> ERROR!, so- Wrap it with if to avoid crash
- Use .discard() to delete the number 999
'''
codes = set([101, 102, 103, 104])
codes.pop()
if 999 in codes:
    codes.remove(999)
codes.discard(999)

# print(list(codes[0]))


# **BONUS**
# **BONUS**
# **BONUS**
# **BONUS**
# **BONUS**
import random

random_nums = []

for i in range(3):
    num = random.randint(1, 10)
    random_nums.append(num)

print(random_nums)

# list_random -> set
#   1. set -> list -> sort
#      for each number print count
#   2. set -> for each min(set)

print(sorted(set(random_nums)))

# print each number and how many times, without duplications
# hint: sort, set, count
# [1, 4, 2, 2, 1, 5]
# 1: 2-times
# 2: 2-times
# 4: 1-time
# 5: 1-time
