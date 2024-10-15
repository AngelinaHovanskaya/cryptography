arr_2 = [4, 1, 2, 3, 5, 0]


def encode(string):

    final_str = ''
    for i in arr_2:
        final_str += string[i]
    return final_str


def decode(string):
    final_str = ''
    for i in range(6):
        num = arr_2.index(i)
        final_str += string[num]
    return final_str


print("Привет! Это шифр перестановки для слов из 6 букв")
choose = int(input('Введите 1 для кодирования или 2 для декодирования: '))
if choose == 1:
    str_1 = input('Введите открытый текст: ').upper()
    str_2 = encode(str_1)
elif choose == 2:
    str_1 = input('Введите закрытый текст: ').upper()
    str_2 = decode(str_1)
else:
    print('Неверный ввод')
    exit()
print(str_2)
