import numpy as np

sbox_encode = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
               ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
               ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
               ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
               ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
               ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
               ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
               ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
               ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
               ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
               ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
               ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
               ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
               ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
               ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
               ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]


mix_columns_arr = [[2, 3, 1, 1],
                   [1, 2, 3, 1],
                   [1, 1, 2, 3],
                   [3, 1, 1, 2]]

rcon_arr = [
    ['01', '0', '0', '0'],
    ['02', '0', '0', '0'],
    ['04', '0', '0', '0'],
    ['08', '0', '0', '0'],
    ['10', '0', '0', '0'],
    ['20', '0', '0', '0'],
    ['40', '0', '0', '0'],
    ['80', '0', '0', '0'],
    ['1b', '0', '0', '0'],
    ['36', '0', '0', '0']]

rcon_counter = 0

key_t = [['2b', '7e', '15', '16'],
         ['28', 'ae', 'd2', 'a6'],
         ['ab', 'f7', '15', '88'],
         ['9',  'cf', '4f', '3c']]


def hex_to_int(char):
    mp = {"0": 0,
          "1": 1,
          "2": 2,
          "3": 3,
          "4": 4,
          "5": 5,
          "6": 6,
          "7": 7,
          "8": 8,
          "9": 9,
          "a": 10,
          "b": 11,
          "c": 12,
          "d": 13,
          "e": 14,
          "f": 15}
    char_int = mp[char]
    return char_int


def str_to_arr(s):
    arr = np.empty((4, 4), dtype=object)
    index = 0
    for i in range(4):
        for j in range(4):
            arr[i][j] = s[index:index + 2]
            index += 2
    arr_t = np.transpose(arr)
    return arr_t


def sub_bytes(arr):
    for i in range(4):
        for j in range(4):
            if len(arr[i][j]) != 2:
                arr[i][j] = '0' + arr[i][j]
            row = hex_to_int(arr[i][j][0])
            col = hex_to_int(arr[i][j][1])
            arr[i][j] = sbox_encode[row][col]
    return arr


def shift_rows(arr):
    shift_rows_arr = np.empty((4, 4), dtype=object)
    for i in range(4):
        for j in range(4):
            shift_rows_arr[i][j] = arr[i][(j + i) % 4]
    return shift_rows_arr


def r_xor_l(r, l):
    res = ''
    for m in range(len(r)):
        if r[m] == l[m]:
            res += '0'
        else:
            res += '1'
    return res


def len_bin(n):
    if len(n) < 8:
        n = (8 - len(n)) * '0' + n
    return n


def gmul(a, b):
    if b == 1:
        a1 = int(a, 16)
        a1 = len_bin(bin(a1)[2:])
        return a1
    elif b == 2:
        return mult_2(a)
    return mult_3(a)


def mult_2(a):
    a = int(a, 16)
    a = len_bin(bin(a)[2:])
    a1 = a[1:] + '0'
    if a[0] == '1':
        b1 = len_bin(bin(27)[2:])
        return r_xor_l(a1, b1)
    return a1


def mult_3(a):
    b = mult_2(a)
    a1 = int(a, 16)
    a1 = len_bin(bin(a1)[2:])
    res_bin = r_xor_l(a1, b)
    return res_bin


def mix_columns(arr):
    new_arr = np.empty((4, 4), dtype=object)
    for i in range(4):
        for j in range(4):
            a0 = gmul(arr[i][0], mix_columns_arr[j][0])
            a1 = gmul(arr[i][1], mix_columns_arr[j][1])
            a2 = gmul(arr[i][2], mix_columns_arr[j][2])
            a3 = gmul(arr[i][3], mix_columns_arr[j][3])
            new_char = r_xor_l(r_xor_l(r_xor_l(a0, a1), a2), a3)
            new_arr[i][j] = hex(int(new_char, 2))[2:]

    return new_arr


def xor_col(arr1, arr2):
    arr3 = []
    for i in range(4):
        a = len_bin(bin(int(arr1[i], 16))[2:])
        b = len_bin(bin(int(arr2[i], 16))[2:])
        arr3.append(hex(int(r_xor_l(a, b), 2))[2:])
    return arr3


def rot_col(arr, counter):
    row_arr = arr[3][1:]
    row_arr.append(arr[3][0])
    for i in range(4):
        if len(row_arr[i]) != 2:
            row_arr[i] = '0' + row_arr[i]
        row = hex_to_int(row_arr[i][0])
        col = hex_to_int(row_arr[i][1])
        row_arr[i] = sbox_encode[row][col]
    row_1 = xor_col(xor_col(row_arr, arr[0]), rcon_arr[counter])
    row_2 = xor_col(row_1, arr[1])
    row_3 = xor_col(row_2, arr[2])
    row_4 = xor_col(row_3, arr[3])
    new_arr = [row_1, row_2, row_3, row_4]
    counter += 1
    return new_arr, counter


def add_round_key(arr1, arr2):
    arr_add_key = np.empty((4, 4), dtype=object)
    for i in range(4):
        for j in range(4):
            a = len_bin(bin(int(arr1[i][j], 16))[2:])
            b = len_bin(bin(int(arr2[i][j], 16))[2:])
            arr_add_key[i][j] = hex(int(r_xor_l(a, b), 2))[2:]
    return arr_add_key


input_str = '193de3bea0f4e22b9ac68d2ae9f84808'


arr_1 = str_to_arr(input_str)
for i in range(9):

    arr_sub_bytes = sub_bytes(arr_1)
    arr_shift_rows = shift_rows(arr_sub_bytes)
    arr_shift_rows_t = np.transpose(arr_shift_rows)
    arr_mix_column = mix_columns(arr_shift_rows_t)
    arr_mix_column_t = np.transpose(arr_mix_column)

    key_t, rcon_counter = rot_col(key_t, rcon_counter)
    round_res = add_round_key(arr_mix_column, key_t)
    arr_1 = np.transpose(round_res)
    print('Round', rcon_counter, '\n', arr_1)


arr_sub_bytes = sub_bytes(arr_1)
arr_shift_rows = shift_rows(arr_sub_bytes)
arr_shift_rows_t = np.transpose(arr_shift_rows)
key_t, rcon_counter = rot_col(key_t, rcon_counter)
round_res = add_round_key(arr_shift_rows_t, key_t)
arr_1 = np.transpose(round_res)
result = ''
for i in range(4):
    for j in range(4):
        if len(arr_1[i][j]) != 2:
            arr_1[i][j] = '0' + arr_1[i][j]
        result += arr_1[i][j]

print('\nИсходное сообщение:', input_str)
print('Зашифрованное сообщение: ', result)
