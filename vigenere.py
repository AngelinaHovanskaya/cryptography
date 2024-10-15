import pandas as pd
import numpy as np

index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data = {}
for i in range(len(index)):
    index_1 = index[i:] + index[:i]
    data[index[i]] = index_1

df = pd.DataFrame(data, index=index)
print(df)


def encode(string, key):
    final_str = ''
    while len(key) < len(string):
        key += key
    for i in range(len(string)):
        final_str += df[string[i]][key[i]]

    print(f'Исходный текст: {string}')
    print(f'Ключ: {key}')
    print(f'Зашифрованное сообщение: {final_str}')


def decode(string, key):
    final_str = ''
    while len(key) < len(string):
        key += key

    for i in range(len(string)):
        df1 = df.loc[[key[i]]]
        df_result = df1.iloc[np.where(df1 == string[i])].columns[0]
        final_str += df_result

    print(f'Зашифрованное сообщение: {string}')
    print(f'Ключ: {key}')
    print(f'Исходный текст: {final_str}')


print("Привет! Это шифр Виженера")
choose = int(input('Введите 1 для кодирования или 2 для декодирования: '))
if choose == 1:
    str_1 = input('Введите открытый текст: ').upper()
    k = input('Введите ключ: ').upper()
    encode(str_1, k)
elif choose == 2:
    str_1 = input('Введите закрытый текст: ').upper()
    k = input('Введите ключ: ').upper()
    decode(str_1, k)
else:
    print('Неверный ввод')
    exit()
