alph_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alph_2 = ['K', 'G', 'S', 'L', 'Z', 'A', 'Y', 'Q', 'E', 'M', 'H', 'B', 'F',
          'J', 'X', 'W', 'V', 'O', 'I', 'N', 'R', 'T', 'C', 'D', 'U', 'P']


def encode(string):
    final_str = ''
    for i in string:
        if i in alph_1:
            num = alph_1.index(i)
            final_str += alph_2[num]
        else:
            final_str += i
    return final_str


def decode(string):
    final_str = ''
    for i in string:
        if i in alph_2:
            num = alph_2.index(i)
            final_str += alph_1[num]
        else:
            final_str += i
    return final_str


print("Привет! Это шифр замены")
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
