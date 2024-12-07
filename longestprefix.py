def long_pref(list_of_wrds):
    if not list_of_wrds:
        return ""
    prefix = ""
    for i in range(len(list_of_wrds[0])):
        char = list_of_wrds[0][i]
        for j in range(1, len(list_of_wrds)):
            if i >= len(list_of_wrds[j]) or list_of_wrds[j][i] != char:
                return prefix
        prefix += char
    return prefix


list_of_words = []
length_of_list = int(input('Length of your list: '))
for i in range(0, length_of_list):
    list_element = str(input("Word: "))
    list_of_words.append(list_element)
print('Input: ', list_of_words)
print('Output: ', long_pref(list_of_words))

