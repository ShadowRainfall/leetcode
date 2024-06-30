def occur_search(modify_bs, search_string):
    # modify_bs = [str(x) for x in modify_bs]
    for i in range(len(modify_bs)):
        if search_string in modify_bs:
            return modify_bs.index(modify_bs[i])
        else:
            return -1


base_string = input('haystack: ')
string_for_executing = input('needle: ')
print('Output: ', occur_search(base_string, string_for_executing))
