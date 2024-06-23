nums = []
indices = []
visited = set()
index_first = 0
index_second = 0

length = int(input('Length of list elements: '))
target = int(input("Input target: "))
for _ in range(length):
    element = int(input('Element: '))
    nums.append(element)
print("List: ", nums)

for i in range(length):
    for j in range(i + 1, length):
        if nums[i] + nums[j] == target:
            if (i, j) not in visited and (j, i) not in visited:
                indices.append((i, j))
                visited.add((i, j))
                visited.add((j, i))
print(f"Your indices: {indices}")
