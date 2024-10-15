import math
import decimal
from sympy import randprime


decimal.getcontext().prec = 1000000000000000
p = randprime(500, 1000)
q = randprime(100, 500)

n = p * q
fi = (p - 1) * (q - 1)
e = 2

while True:
    if math.gcd(e, fi) == 1:
        break
    e += 1

d = 2
while True:
    if (d * e) % fi == 1:
        break
    d += 1

print(f'p = {p}, q = {q}, n = {n}\n'
      f'fi = {fi}, e = {e}, d = {d}\n')


def str_to_num(string):
    num_arr = []
    for i in string:
        num_arr.append(ord(i))
    return num_arr


def num_to_str(n_arr):
    res_str = ''
    for i in n_arr:
        res_str += chr(int(i))
    return res_str


def encrypt(arr_1):
    encrypt_arr = []
    for i in arr_1:
        encrypt_arr.append((decimal.Decimal(i) ** decimal.Decimal(e)) % decimal.Decimal(n))
    return encrypt_arr


def decrypt(arr_2):
    decrypt_arr = []
    for i in arr_2:
        decrypt_arr.append(((decimal.Decimal(i) ** decimal.Decimal(d)) % decimal.Decimal(n)))
    return decrypt_arr


def print_encode_message(arr_3):
    res = ''
    for i in arr_3:
        res += str(i)
    return res


message = 'hi my name is Angelina'
print('Исходный текст: ', message)
arr = str_to_num(message)
print('Исходный текст в цифрах: ', print_encode_message(arr))
en_arr = encrypt(arr)
print('Зашифрованное сообщение в цифрах:', print_encode_message(en_arr))
de_arr = decrypt(en_arr)
print('Дешифрованное сообщение:', num_to_str(de_arr))
