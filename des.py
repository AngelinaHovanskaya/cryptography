def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin_str = ""
    for k in range(len(s)):
        bin_str += mp[s[k]]
    return bin_str


def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex_str = ""
    for k in range(0, len(s), 4):
        ch = ""
        ch = ch + s[k]
        ch = ch + s[k + 1]
        ch = ch + s[k + 2]
        ch = ch + s[k + 3]
        hex_str += mp[ch]

    return hex_str


s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

initial_permutation_arr = [58, 50, 42, 34, 26, 18, 10, 2,
                           60, 52, 44, 36, 28, 20, 12, 4,
                           62, 54, 46, 38, 30, 22, 14, 6,
                           64, 56, 48, 40, 32, 24, 16, 8,
                           57, 49, 41, 33, 25, 17, 9, 1,
                           59, 51, 43, 35, 27, 19, 11, 3,
                           61, 53, 45, 37, 29, 21, 13, 5,
                           63, 55, 47, 39, 31, 23, 15, 7]


def initial_permutation(s):
    s1 = ''
    for k in range(len(initial_permutation_arr)):
        s1 += s[initial_permutation_arr[k]-1]
    return s1


key_preparation_first_part = [57, 49, 41, 33, 25, 17, 9,
                              1, 58, 50, 42, 34, 26, 18,
                              10, 2, 59, 51, 43, 35, 27,
                              19, 11, 3, 60, 52, 44, 36]

key_preparation_second_part = [63, 55, 47, 39, 31, 23, 15,
                               7, 62, 54, 46, 38, 30, 22,
                               14, 6, 61, 53, 45, 37, 29,
                               21, 13, 5, 28, 20, 12, 4]


def key_preparation(k):
    k_f = ''
    k_s = ''
    for m in range(len(key_preparation_first_part)):
        k_f += k[key_preparation_first_part[m]-1]
        k_s += k[key_preparation_second_part[m]-1]
    return k_f, k_s


key_shift_arr = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def key_shift(k1, k2, c):
    shift = sum(key_shift_arr[:c+1])
    k1_shift = k1[shift:] + k1[:shift]
    k2_shift = k2[shift:] + k2[:shift]
    c += 1
    return k1_shift, k2_shift, c


final_key_processing_arr = [14, 17, 11, 24, 1, 5,
                            3, 28, 15, 6, 21, 10,
                            23, 19, 12, 4, 26, 8,
                            16, 7, 27, 20, 13, 2,
                            41, 52, 31, 37, 47, 55,
                            30, 40, 51, 45, 33, 48,
                            44, 49, 39, 56, 34, 53,
                            46, 42, 50, 36, 29, 32]


def final_key_processing(k):
    f_k = ''
    for m in range(len(final_key_processing_arr)):
        f_k += k[final_key_processing_arr[m]-1]
    return f_k


right_side_expansion_arr = [32, 1, 2, 3, 4, 5,
                            4, 5, 6, 7, 8, 9,
                            8, 9, 10, 11, 12, 13,
                            12, 13, 14, 15, 16, 17,
                            16, 17, 18, 19, 20, 21,
                            20, 21, 22, 23, 24, 25,
                            24, 25, 26, 27, 28, 29,
                            28, 29, 30, 31, 32, 1]


def right_side_expansion(r_s):
    right_side = ''
    for k in range(len(right_side_expansion_arr)):
        right_side += r_s[right_side_expansion_arr[k]-1]
    return right_side


def r_xor_k(right, key_xor):
    res = ''
    for k in range(len(right)):
        if right[k] == key_xor[k]:
            res += '0'
        else:
            res += '1'
    return res


finite_permutation_arr = [16, 7, 20, 21, 29, 12, 28, 17,
                          1, 15, 23, 26, 5, 18, 31, 10,
                          2, 8, 24, 14, 32, 27, 3, 9,
                          19, 13, 30, 6, 22, 11, 4, 25]


def finite_permutation(s):
    final_right_str = ''
    for k in range(len(finite_permutation_arr)):
        final_right_str += s[finite_permutation_arr[k]-1]
    return final_right_str


final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]


def final(s):
    res = ''
    for k in range(len(final_perm)):
        res += s[final_perm[k]-1]
    return res


def key_de_shift(k1, k2, c):
    shift = sum(key_shift_arr[:c])
    k1_shift = k1[shift:] + k1[:shift]
    k2_shift = k2[shift:] + k2[:shift]
    c -= 1
    return k1_shift, k2_shift, c


def encrypt(init_perm_bin, counter, func):
    for i in range(16):

        l0 = init_perm_bin[:32]
        r0 = init_perm_bin[32:]
        key_bin = hex2bin(key)
        key_left, key_right = key_preparation(key_bin)
        key_left_shift, key_right_shift, counter = func(key_left, key_right, counter)
        k_shift = key_left_shift + key_right_shift
        final_key = final_key_processing(k_shift)
        r = right_side_expansion(r0)
        r1 = r_xor_k(r, final_key)
        result = ''
        for j in range(1, 9):

            r2 = r1[((j - 1) * 6):(j * 6)]
            s_str = r2[0] + r2[-1]
            s_col = r2[1:5]
            s_str_dec = int(s_str, 2)
            s_col_dec = int(s_col, 2)
            r3 = bin(s_box[j - 1][s_str_dec][s_col_dec])[2:]
            if len(r) != 4:
                r3 = '0' * (4 - len(r3)) + r3
            result += r3
        right_str = finite_permutation(result)
        final_right_str_bin = r_xor_k(right_str, l0)
        final_right_str_hex = bin2hex(final_right_str_bin)
        r0_hex = bin2hex(r0)
        if i == 15:
            print('Round', i+1, final_right_str_hex, r0_hex, bin2hex(final_key))
            encode_string = final(final_right_str_bin + r0)
            print('\nИтоговая строка: ', bin2hex(encode_string))
            return encode_string, counter

        print('Round', i+1, r0_hex, final_right_str_hex, bin2hex(final_key))
        init_perm_bin = r0 + final_right_str_bin


key = "AABB09182736CCDD"
input_str = '123456ABCD132536'
print('Исходная строка', input_str)
print('Ключ: ', key)

print('\nКодирование:')
cnt = 0
input_str_bin = hex2bin(input_str)
str_init_perm_bin = initial_permutation(input_str_bin)
fin_str, cnt = encrypt(str_init_perm_bin, cnt, key_shift)

print('\nДекодирование:')
input_str_bin = fin_str
str_init_perm_bin = initial_permutation(input_str_bin)
encrypt(str_init_perm_bin, cnt, key_de_shift)
