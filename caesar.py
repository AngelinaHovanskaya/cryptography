def encode(string, key):
    final_str = ''
    for i in string:
        if i.islower():
            if ord(i) <= 122:
                char = (((ord(i) + key) - 97) % 26) + 97
            else:
                char = (((ord(i) + key) - 1072) % 32) + 1072
        elif i.isupper():
            if ord(i) <= 90:
                char = (((ord(i) + key) - 65) % 26) + 65
            else:
                char = (((ord(i) + key) - 1040) % 32) + 1040
        else:
            char = ord(i)
        final_str += chr(char)
    return final_str


def decode(string, key):
    final_str = ''
    for i in string:
        if i.islower():
            if ord(i) <= 122:
                char = (((ord(i) - key) - 97) % 26) + 97
            else:
                char = (((ord(i) - key) - 1072) % 32) + 1072
        elif i.isupper():
            if ord(i) <= 90:
                char = (((ord(i) - key) - 65) % 26) + 65
            else:
                char = (((ord(i) - key) - 1040) % 32) + 1040
        else:
            char = ord(i)
        final_str += chr(char)
    return final_str


print("Привет! Это шифр Цезаря")
choose = int(input('Введите 1 для кодирования или 2 для декодирования: '))
if choose == 1:
    str_1 = input('Введите открытый текст: ')
    k = int(input('Введите ключ: '))
    str_2 = encode(str_1, k)
elif choose == 2:
    str_1 = input('Введите закрытый текст: ')
    k = int(input('Введите ключ: '))
    str_2 = decode(str_1, k)
else:
    print('Неверный ввод')
    exit()
print(str_2)
