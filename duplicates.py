def duplicate_search(numbers):
    if not numbers:
        return 0
    k = 0
    new_nums = []
    for i in range(0, len(numbers)):
        if numbers[i] not in new_nums:
            new_nums.append(numbers[i])
            k += 1
    print('Unique numbers: ', k)
    new_nums.sort()
    print('Output: ', new_nums)


nums = []
length_of_list = int(input('Length of your list: '))
for i in range(0, length_of_list):
    list_element = int(input("Number: "))
    nums.append(list_element)
print('Input: ', nums)
duplicate_search(nums)
