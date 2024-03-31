from prettytable import PrettyTable
from math import *


line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."

N = len(line)

# Функция превращения в двоичный байтовый код ASCII
#-------------------------------------------------------------------------------#
def make_bytes(text:str, encoding = 'cp1251') -> str:
    return ''.join(bin(c)[2:].rjust(8, '0') for c in text.encode(encoding))
#-------------------------------------------------------------------------------#

# Основная функция
#-------------------------------------------------------------------------------#
def Code(line, N, array_number_ascci):

    table = PrettyTable()
    table.field_names = ["Символ последовательности", "N в ASCII", "Номер в стопке кнги", "Кодовое слово", "Длина кодового слова"]

    array_ascii = []

    for el in range(256):
        array_ascii.append(el)

    array_char = []
    array_position = []

    for char in line:
        array_char.append(char)

    for index in range(len(line)):
        array_position.append(array_ascii.index(array_number_ascci[index]))
        array_ascii.remove(array_number_ascci[index])
        array_ascii.insert(0, array_number_ascci[index])

    array_of_len = []
    for element in array_position:
        code = bin(element)[3:]
        result = '1'*(len(code)+1) + "0" + code
        array_of_len.append(result)

    count_of_len = 0
    code = ''

    for index in range(len(line)):
        count_of_len += len(array_of_len[index])
        code += array_of_len[index]
        table.add_row([line[index], array_number_ascci[index], array_position[index], array_of_len[index], len(array_of_len[index])])

    print(table)
    print(f'l = {count_of_len}')
    print(f"cx = {code}")

#-------------------------------------------------------------------------------#

# Создаем таблицу ASCII
#----------------------------------------------#
bytes_line = make_bytes(line)
array_number_ascii = []

for i in range(0, len(bytes_line), 8):
    degree = 7
    number = 0
    for j in bytes_line[i:i+8]:
        number += int(j)*2**degree
        degree -= 1
    array_number_ascii.append(number)
#----------------------------------------------#

# print(line)
# print(array_number_ascii)

Code(line, N, array_number_ascii)
