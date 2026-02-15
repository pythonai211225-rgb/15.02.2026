
nums = [5, 2, 1, 9, -4]
nums.sort(reverse=True)  # Big -> Small
nums.sort(reverse=False)  # Small -> Big
nums.sort()  # reverse=False  Small -> Big
print(nums)

# in a given list, check if there are duplications?
# Solution 1
# nums = [5, 2, 1, 9, -4, 2]
# find if there is duplicate, without using count
#    for x in numbers: if nums.count(x) > 1
#    *Bonus --> any/ all
nums = [5, 2, 1, 9, -4, 2]
_is_duplicate = False
for x in nums:
    if nums.count(x) > 1:
        _is_duplicate = True
        break
print(f"Are there duplicated here {nums} ? {_is_duplicate}")

nums = [5, 2, 1, 9, -4, -9]
_is_duplicate = False
for x in nums:
    if nums.count(x) > 1:
        _is_duplicate = True
        break
print(f"Are there duplicated here {nums} ? {_is_duplicate}")

# Solution 2
# sort
# nums = [-4, 1, 2, 2, 5, 9]
# run on all index check if the number is equal to his previous
#     if yes --> we found! exit
#     if reach the end and did not find --> there is no duplicate
#    *Bonus --> any/ all

#       0  1  2  3   4  5
nums = [5, 2, 1, 9, -4, 2]
nums.sort()
# [-4, 1, 2, 2, 5, 9]
_is_duplicate = False
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        _is_duplicate = True
        break
print(f"Are there duplicated here {nums} ? {_is_duplicate}")

nums = [5, 2, 1, 9, -4, -9]
nums.sort()
# [-9, -4, 1, 2, 5, 9]
_is_duplicate = False
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        _is_duplicate = True
        break
print(f"Are there duplicated here {nums} ? {_is_duplicate}")


# sort without changing the original
backup = nums.copy()
nums.sort()

nums = [5, 2, 9, 1]
new_nums = sorted(nums)
new_nums = sorted(nums, reverse=True)
print(nums)      # [5, 2, 9, 1]
print(new_nums)  # [1, 2, 5, 9]

# Sort opposite = sort + reverse
nums = [5, 2, 9, -1, 1]
nums.sort()
nums.reverse()
print(nums)
print(sorted(nums)[::-1])

# sort by abc
names = ["Dana", "adam", "Ben", "carol"]
print(sorted(names))  # the capital comes first

# sort by abc
#         4       4      3       5
names = ["Dana!!!", "adam*", "Ben", "caro***l", "A"]
print(sorted(names, key=len))  # the capital comes first

# nums = [7, 1, 9, 2, 2, 10]
# words = ["banana", "kiwi", "apple", "fig", "watermelon"]
'''
Do:
Print nums sorted ascending (without changing original)
Sort nums in-place descending
Print words alphabetically A→Z
Print words by length shortest→longest
Print words by length longest→shortest. hint: reverse=True
'''