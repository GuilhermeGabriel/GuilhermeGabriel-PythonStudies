num_input = input("Digite o número: ")


# 01
# Transforma um número de binário para decimal
def bin_to_decimal(num):
    num_list = list(num)
    sum = 0
    num_inverted = list(reversed(num_list))
    for i in range(0, len(num_inverted)):
        sum += int(num_inverted[i]) * pow(2, i)

    return sum


# print(bin_to_decimal(num_input))
# print(int(str(num_input), 2))

# 02
# Transforma qualquer base para decimal
def base_to_decimal(num, base):
    sum = 0
    num_inverted = list(reversed(num))
    for i in range(0, len(num_inverted)):
        sum += int(num_inverted[i]) * pow(base, i)

    return sum


# print(base_to_decimal(num_input, 16))
# print(int(str(num_input), 16))


# 03
# Transformar decimal para binário
def decimal_to_bin(num):
    num_list = []

    while int(num) >= 2:
        rest = int(num) % 2
        num = int(num) // 2

        num_list.insert(0, rest)

    num_list.insert(0, num)  # num_list é um vetor com os algarismos do resultado
    num_value = ''.join(list(map(str, num_list)))  # Transforma cada algarismo em uma
    # string e depois junta e trasforma essa string um int

    return int(num_value)


# print(decimal_to_bin(num_input))
# print(bin(int(num_input)))


# 04
# Transformar decimal para qualquer base
def decimal_to_base(num, base):
    num_list = []

    while int(num) >= base:
        rest = int(num) % base
        num = int(num) // base

        num_list.insert(0, rest)

    num_list.insert(0, get_algarism_from_num_hex(int(num)))
    num_value = ''.join(list(map(str, num_list)))  # Transforma cada algarismo em uma
    # string e depois junta e trasforma essa string um int

    return num_value


def get_algarism_from_num_hex(num):
    alga_hex_list = ['A', 'B', 'C', 'E', 'F']
    if 10 <= num <= 16:
        return alga_hex_list[num - 10]
    else:
        return num


def get_num_hex(alga):
    alga_hex_list = ['A', 'B', 'C', 'D', 'E', 'F']
    num_hex_list = [10, 11, 12, 13, 14, 15]

    if alga.upper() in alga_hex_list:
        return num_hex_list[alga_hex_list.index(alga.upper())]
    else:
        return int(alga)


# print(decimal_to_base(num_input, 12))


# 05
# Transforma de qualquer base para qualquer base
def base_to_base(num, base1, base2):
    num_in_decimal = base_to_decimal(num, base1)
    num_in_base2 = decimal_to_base(num_in_decimal, base2)
    return num_in_base2


# print(base_to_base(num_input, 10, 16))

# 06
# Transforma hexa para binario (blocagem)
def hex_to_bin_blocagem(num):
    block = []

    for i in range(len(num) - 1, -1, -1):

        block_in_bin = list(str(
            decimal_to_bin(get_num_hex(num[i]))
        ))

        while len(block_in_bin) < 4:
            block_in_bin.insert(0, '0')

        block.insert(0, block_in_bin)

    return block


# print(hex_to_bin_blocagem(num_input))
# print(bin(int(str(num_input), 16)))


# 07
# Transforma de octa para binario (blocagem)
def octal_to_bin(num):
    block = []

    for i in range(len(num) - 1, -1, -1):

        block_in_bin = list(str(
            decimal_to_bin(get_num_hex(num[i]))
        ))

        while len(block_in_bin) < 3:
            block_in_bin.insert(0, '0')

        block.insert(0, block_in_bin)

    return block


#print(octal_to_bin(num_input))
#print(bin(int(str(num_input), 8)))
