import math
import struct


def check_len(n, len_n):
    if len(n) != len_n:
        n = '0' * (len_n - len(n)) + n
    return n


def func_f(b, c, d):
    return (b & c) | ((b ^ 0xffffffff) & d)


def func_g(b, c, d):
    return (b & d) | (c & (d ^ 0xffffffff))


def func_h(b, c, d):
    return b ^ c ^ d


def func_i(b, c, d):
    return c ^ (b | (d ^ 0xffffffff))


def generate_md5_constants():
    t = []
    for j in range(1, 65):
        # Вычисляем i-ый элемент таблицы: 2^32 * abs(sin(i))
        value = int(2**32 * abs(math.sin(j)))
        t.append(value)
    return t


def str_to_hex(string):
    hex_string = ''
    for j in string:
        hex_string += hex(ord(j))[2:]
    return hex_string


input_str = 'AlekOS'
first_str = bytearray(bytes.fromhex(input_str.encode("UTF-8").hex()))
length = len(first_str)
text_length = (8 * length) & 0xFFFFFFFFFFFFFFFF
rest = length % 64
if rest < 56:
    size = -rest + 56 - 1
else:
    size = 64-rest + 56 - 1
first_str.append(0x80)
for _ in range(size):
    first_str.append(0)
first_str += struct.pack('<Q', text_length)

m = struct.unpack('<16I', first_str)


A = int(0x67452301)
B = int(0xEFCDAB89)
C = int(0x98BADCFE)
D = int(0x10325476)

# Генерируем таблицу T
T = generate_md5_constants()


S = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
     5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

block_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
              1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12,
              5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2,
              0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9]

for i in range(64):
    if i < 16:
        x = func_f(B, C, D)
    elif i < 32:
        x = func_g(B, C, D)
    elif i < 48:
        x = func_h(B, C, D)
    else:
        x = func_i(B, C, D)
    x1 = (int(x) + A) % (2**32)
    x2 = (x1 + (m[block_list[i]])) % (2**32)

    x3 = (x2 + T[i]) % (2**32)

    x4 = check_len(bin(x3)[2:], 32)

    x5 = int(x4[S[i]:] + x4[:S[i]], 2)
    x6 = (x5 + B) % (2 ** 32)
    A, B, C, D = D, x6, B, C
    # print(f'Step{i}', hex(A), hex(B), hex(C), hex(D), '\n')


A1 = int(0x67452301)
B1 = int(0xEFCDAB89)
C1 = int(0x98BADCFE)
D1 = int(0x10325476)


AA = (A1 + A) & 4294967295
BB = (B1 + B) & 4294967295
CC = (C1 + C) & 4294967295
DD = (D1 + D) & 4294967295
hashed_string = struct.pack('<4I', AA, BB, CC, DD).hex()

print("Input str\t\t", input_str)
print("Output str\t\t", hashed_string)
