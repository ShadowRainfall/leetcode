nums = []
length = int(input('Length of list elements: '))
target = int(input("Input target: "))
print("Target: ", target)
index_first = 0
index_second = 0
if index_first in range(0, length):
    for index_second in range(0, length):
        element = int(input('Element: '))
        nums.append(element)
        if nums[index_first] + nums[index_second] == target:
            index_first = index_first
            index_second = index_second
print("List: ", nums)
print(f"Your indices: {index_first, index_second}")


