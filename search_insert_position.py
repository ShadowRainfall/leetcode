def search_pos(numbers, targ):
    for i in range(0, len(numbers)):
        if targ in numbers:
            return numbers.index(targ)
        else:
            numbers.append(targ)
            numbers.sort()
            ind = numbers.index(targ)
            numbers.remove(targ)
            return ind


nums = []
length_of_list = int(input('Length of your list: '))
for i in range(0, length_of_list):
    list_element = int(input("Number: "))
    nums.append(list_element)
print('Input: ', nums)
target = int(input('target: '))
print('Output: ', search_pos(nums, target))
