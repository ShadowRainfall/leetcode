def palindrome_num():
    x = input("X number: ")
    try:
        modify_x_list = [int(x) for x in str(x)]
        if modify_x_list == modify_x_list[::-1]:
            print('True')
            return True
        else:
            print('False')
            return False
    except ValueError as v:
        print(f'ERROR: {v}')


palindrome_num()
