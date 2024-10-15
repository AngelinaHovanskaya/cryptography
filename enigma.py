import string

abc = list(string.ascii_uppercase)


class ThirdRotor:
    def __init__(self):
        self.dictionary = [(1, 3), (5, 20), (17, 2), (2, 15), (14, 18), (8, 1), (12, 13),
                           (18, 10), (9, 5), (13, 24), (3, 19), (23, 6), (6, 17), (16, 12),
                           (25, 21), (15, 26), (4, 8), (10, 25), (21, 9), (26, 14), (22, 11),
                           (19, 16), (11, 23), (24, 7), (7, 4), (20, 22)]
        self.code_position = 0
        self.decode_position = 0
        self.decode_counter = 0
        self.counter = 0

    def cycle_search(self, search):
        while search > 26:
            search -= 26
        return search

    def code(self, input, direction):
        search = self.cycle_search((input + self.code_position))
        for i in range(26):
            if self.dictionary[i][switch_direction(direction)] == search:
                if direction == 1:
                    self.code_position += 1
                    self.counter += 1
                    if self.counter > 26:
                        self.counter -= 26
                return self.dictionary[i][direction], self.counter

    def decode(self, input, direction):
        result = 0
        if self.decode_position > 26:
            self.decode_position -= 26
        real_position = self.decode_position
        for i in range(26):
            if self.dictionary[i][switch_direction(direction)] == input:
                result = self.dictionary[i][direction] - real_position

                while result <= 0:
                    result += 26

                if direction == 1:
                    self.decode_position += 1
                    self.decode_counter += 1
                    if self.decode_counter > 26:
                        self.decode_counter -= 26

        return result, self.decode_counter


class SecondRotor:
    def __init__(self):
        self.dictionary = [(1, 3), (5, 20), (17, 2), (2, 15), (14, 18), (8, 1), (12, 13),
                           (18, 10), (9, 5), (13, 24), (3, 19), (23, 6), (6, 17), (16, 12),
                           (25, 21), (15, 26), (4, 8), (10, 25), (21, 9), (26, 14), (22, 11),
                           (19, 16), (11, 23), (24, 7), (7, 4), (20, 22)]
        self.code_position = 0
        self.decode_position = 0

    def cycle_search(self, search):
        while search > 26:
            search -= 26
        return search

    def cycle_iterator(self, iterator):
        while iterator > 26:
            iterator //= 26
        return iterator

    def code(self, input, direction, counter):
        if direction == 0:
            if counter == 26:
                self.code_position += 1
        real_position = self.code_position

        search = self.cycle_search((input + self.cycle_iterator(real_position)))
        result = 0
        for i in range(26):
            if self.dictionary[i][switch_direction(direction)] == search:
                result = self.dictionary[i][direction]
        return result

    def decode(self, input, direction, counter):
        result = 0
        if direction == 0:
            if counter == 26:
                self.decode_position += 1
        real_position = self.decode_position
        for i in range(26):
            if self.dictionary[i][switch_direction(direction)] == input:
                result = self.dictionary[i][direction] - self.cycle_iterator(real_position)

                while result <= 0:
                    result += 26

        return result


class Stator:
    def __init__(self):
        self.dictionary = [(5, 24), (14, 19), (9, 23), (26, 13), (22, 7), (20, 12),
                           (17, 1), (21, 25), (16, 2), (18, 3), (11, 8), (10, 6), (4, 15),
                           (24, 5), (19, 14), (23, 9), (13, 26), (7, 22), (12, 20),
                           (1, 17), (25, 21), (2, 16), (3, 18), (8, 11), (6, 10), (15, 4)]

    def find(self, input):
        for i in range(26):
            if self.dictionary[i][0] == input:
                return self.dictionary[i][1]


rotor_3 = ThirdRotor()
rotor_2 = SecondRotor()
stator = Stator()


def encode_by_rotors(letter):
    number = abc.index(letter) + 1
    third_rtl, counter = rotor_3.code(number, 0)
    second_rtl = rotor_2.code(third_rtl, 0, counter)
    stator_rtl = stator.find(second_rtl)
    second_ltr = rotor_2.code(stator_rtl, 1, counter)
    third_ltr, counter = rotor_3.code(second_ltr, 1)
    return abc[third_ltr - 1]


def decode_by_rotors(letter):
    number = abc.index(letter) + 1
    third_rtl, counter = rotor_3.decode(number, 0)
    second_rtl = rotor_2.decode(third_rtl, 0, counter)
    stator_rtl = stator.find(second_rtl)
    second_ltr = rotor_2.decode(stator_rtl, 1, counter)
    third_ltr, counter = rotor_3.decode(second_ltr, 1)
    return abc[third_ltr - 1]


def encrypt_word(word):
    result = []
    for letter in word:
        if letter in abc:
            res = encode_by_rotors(letter)
            result.append(res)
        else:
            result.append(letter)
    return result


def decrypt_word(word):
    result = []
    for letter in word:
        if letter in abc:
            res = decode_by_rotors(letter)
            result.append(res)
        else:
            result.append(letter)
    return result


def switch_direction(direction):
    if direction == 1:
        return 0
    return 1


result_1 = []


print("Привет! Это шифровальная машина Энигма")
choose = int(input('Введите 1 для кодирования или 2 для декодирования: '))
if choose == 1:
    str_1 = input('Введите открытый текст: ').upper().split()
    for word in str_1:
        encrypted = encrypt_word(word)
        result_1.append(encrypted)
elif choose == 2:
    str_1 = input('Введите закрытый текст: ').upper().split()
    for word in str_1:
        decrypted = decrypt_word(word)
        result_1.append(decrypted)
else:
    print('Неверный ввод')
    exit()

encode_string = ''
for i in result_1:
    encode_string += ''.join(i) + ' '
print(encode_string)
