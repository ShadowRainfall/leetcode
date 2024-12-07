def decoding(x):
    if ('I' == x):
        return 1
    elif ('V' == x):
        return 5
    elif ('X' == x):
        return 10
    elif ('L' == x):
        return 50
    elif ('C' == x):
        return 100
    elif ('D' == x):
        return 500
    elif ('M' == x):
        return 1000
    return -1


def rom_to_int(string_of_symbols):
    result = 0
    count = 0
    while (count < len(string_of_symbols)):
        symb_1 = decoding(string_of_symbols[count])
        if (count + 1 < len(string_of_symbols)):
            symb_2 = decoding(string_of_symbols[count + 1])
            if (symb_1 >= symb_2):
                result += symb_1
                count += 1
            else:
                result += symb_2 - symb_1
                count += 2
        else:
            result += symb_1
            count += 1
    return result


symbols = input("Your ROMAN numbers: ")
print(rom_to_int(symbols))

