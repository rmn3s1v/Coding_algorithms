from prettytable import PrettyTable
from math import *

# line = 'НЕ_ИМЕЙ_СТО_РУБЛЕЙ,_А_ИМЕЙ_СТО_ДРУЗЕЙ.'
# line = "Там_королевич_мимоходом_пленяет_грозного_царя._у_наших_ушки_на_макушке!_чуть_утро_осветило_пушки_и_леса_синие_верхушки_-_французы_тут_как_тут."
# line = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
# line = "Там_ступа_с_Бабою_Ягой_идёт,_бредёт_сама_собой._Два_дня_мы_были_в_перестрелке._Что_толку_в_этакой_безделке?_Мы_ждали_третий_день."
line = "И_тридцать_витязей_прекрасных_чредой_из_вод_выходят_ясных,_и_с_ними_дядька_их_морской._И_вот_нашли_большое_поле:_есть_разгуляться_где_на_воле!_Построили_редут."

# Формируем столбцы таблицы
#------------------------------------------------------------------------------------------------------------------------
table = PrettyTable()
table.field_names = ["Номер шага", "Флаг", "Словарь", "d", "l", "Кодовая последовательность", "Затраты в битах"]
#------------------------------------------------------------------------------------------------------------------------

# Формируем ASCII код
#------------------------------------------------------------------------------------------------------------------------
array_of_ascii = []
for char in line:
    array_of_ascii.append(ord(char.encode('cp1251')))
#------------------------------------------------------------------------------------------------------------------------

array_of_char = []
skip = 1
step_number = 1
l = 0

for index in range(len(line)):
    if skip == 1:
        next_step = 1
        flag = 0

        if line[0:index + next_step].count(line[index]) > 1:
            flag = 1

            while line[0:index].count(line[index:index + next_step]) > 0 and index + next_step <= len(line):
                next_step += 1
            skip = next_step - 1
            array_of_char.append(line[index:index + next_step - 1])

        else:
            array_of_char.append(line[index])

        difference = abs(line[0:index].rfind(array_of_char[len(array_of_char)-1]))

        if flag == 1:
            lenght = ceil(log2(index))
            code = bin(len(array_of_char[len(array_of_char)-1]))[3:]
            result = '1' * (len(code) + 1) + "0" + code
            bin_code = "1" + "0" * (lenght - len(bin(index - difference - 1)[2:])) + bin(index - difference - 1)[2:] + result
            count_of_words = index

            if len(array_of_char[len(array_of_char)-1]) > 1:
                   count_of_words += 1

            table.add_row([step_number, flag, array_of_char[len(array_of_char)-1], str(index - difference - 1) + "(" + str(count_of_words) + ")", len(array_of_char[len(array_of_char)-1]), bin_code, len(bin_code)])
            l += len(bin_code)

        else:
            bin_code = '0' + ''.join(bin(c)[2:].rjust(8, '0') for c in array_of_char[len(array_of_char)-1].encode("cp1251"))
            table.add_row([step_number, flag, array_of_char[len(array_of_char)-1], "-", 0, bin_code, len(bin_code)])
            l += len(bin_code)

        step_number += 1

    else:
        skip -= 1

print(table)
print(f"l = {l}")
# print(array_of_char)
