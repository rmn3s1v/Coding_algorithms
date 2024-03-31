from prettytable import PrettyTable
from math import *

# line = 'НЕ ИМЕЙ СТО РУБЛЕЙ, А ИМЕЙ СТО ДРУЗЕЙ.'
#line = "там королевич мимоходом пленяет грозного царя. у наших ушки на макушке! чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
# line = "Там королевич мимоходом пленяет грозного царя. У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."
# line = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."
N = len(line)

def make_bytes(text:str, encoding = 'cp1251') -> str:
    return ''.join(bin(c)[2:].rjust(8, '0') for c in text.encode(encoding))

class Node(object): # Создать класс узла
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    def __init__(self, text):
        self.leaves = [Node(key, value) for key, value in text.items()]
        while len(self.leaves) > 1:
            self.leaves.sort(key= lambda node: node.value, reverse=True)
            n = Node(value=(self.leaves[-1].value + self.leaves[-2].value))
            n.lchild = self.leaves.pop(-1)
            n.rchild = self.leaves.pop(-1)
            self.leaves.append(n)

        self.root = self.leaves[0]
        self.Buffer = list(range(10))

    def Hu_generate(self, tree, length, result):
        node = tree
        if (not node):
            return
        elif node.name:
            buffer = ''
            for i in range(length):
                buffer += str(self.Buffer[i])
            result[node.name] = buffer
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1, result)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1, result)


def array_set(N, line, c):
    array_cheat = ['000', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '10010', '10011', '10100', '10101', '10110', '10111', '11000',
                   '110010', '110011', '110100', '110101', '110110', '110111', '111000', '111001', '111010', '1110110', '1110111', '1111000', '1111001',
                   '1111010', '1111011', '1111100', '1111101', '1111110', '1111111']
    array_set = []
    dictionary = {}

    if c == 1:
        for i in range(N):
            if line[i] not in array_set:
                array_set.append(line[i])

        for i in array_set:
            dictionary[i] = line.count(i)

    result = {}
    tree = HuffmanTree(dictionary)
    tree.Hu_generate(tree.root, 0 ,result)

    array_code = []
    array_char = []

    for char in sorted(result):
        array_code.append(result[char])
        array_char.append(char)

    for i in range(len(array_code)):
        for j in range(len(array_code)-1):
            if len(array_code[j]) > len(array_code[j+1]):
                array_code[j], array_code[j+1] = array_code[j+1], array_code[j]
                array_char[j], array_char[j+1] = array_char[j+1], array_char[j]

    array_cx1 = []
    # формируем код вида 0001 для дерева
    for code in array_code:
        new_code = ''
        for i in range(len(code)):
            new_code += '0'
        new_code += '1'
        array_cx1.append(new_code)

    #print(array_code) # вывод массива кода хафмана
    #print(array_cx1) # вывод кодов вида 001

    # находим максимально длинное кодовое слово
    max_len_for_vertelex = len(array_cx1[0]) # максимальная длина кодового слова = количеству ярусов
    for i in range(len(array_cx1)):
        if (len(array_cx1[i]) > max_len_for_vertelex):
            max_len_for_vertelex = len(array_cx1[i])

    # подсчитываем кол-во конечных вершин на каждом ярусе
    array_vertexe_end = []
    for i in range(max_len_for_vertelex):
        count = 0
        for j in array_cx1:
            if len(j) > i:
                if j[i] == "1":
                    count += 1
        array_vertexe_end.append(count)

    array_count_vertexex = [1] # массив кол-ва вершин на каждом ярусе

    # подсчитваем кол-во вершин на каждом ярусе
    for i in range(1, max_len_for_vertelex):
        count = 0
        # узнаем колличество вершин, которых не будет на ярусе (узнаем конечные вершины)
        for j in range(i):
            count += array_vertexe_end[j]*2**(i-j)
        array_count_vertexex.append(2**i-count)

    #print(array_vertexe_end)
    #print(array_count_vertexex)

    mytable = PrettyTable()
    mytable.field_names = ["Ярус", "Общее число вершин", "Число концевых вершин ni", "Диапазон значений ni", "Затраты в битах", "Комбинация для концевых вершин"]

    ascii_count = 256
    count_of_combination = 0
    count_of_bit = 0
    for i in range(max_len_for_vertelex):
        two = 1
        degree_of_two = 0
        combinations = 0
        while two < array_count_vertexex[i] + 1:
            two *= 2
            degree_of_two += 1
        if (array_vertexe_end[i] != 0):
            # print(ascii_count)
            # print(array_vertexe_end[i])
            # print(log2((factorial(ascii_count))/(factorial(array_vertexe_end[i])*factorial(ascii_count-array_vertexe_end[i]))))
            combinations = ceil(log2((factorial(ascii_count))/(factorial(array_vertexe_end[i])*factorial(ascii_count-array_vertexe_end[i]))))
            ascii_count -= array_vertexe_end[i]
            # print(ascii_count)
        count_of_combination += combinations
        count_of_bit += degree_of_two
        mytable.add_row([i, array_count_vertexex[i], array_vertexe_end[i], "0-"+str(array_count_vertexex[i]), degree_of_two, combinations])
        #print(f"{i}|{array_count_vertexex[i]}|{array_vertexe_end[i]}|0-{array_count_vertexex[i]}|{degree_of_two}|{combinations}")

    code_cx2 = ''
    for i in array_char:
        code_cx2 += make_bytes(i)
    #print(len(code_cx2))

    code_cx1 = ""
    for i in line:
        code_cx1 += result[i]
    #print(len(code_cx1))

    print(mytable)
    print(f"Всего на бит на КОМБИНАЦИИ: {count_of_combination}")
    print(f"Вссего бит на ВЕРШИНЫ: {count_of_bit}")
    print(f"Всего бит в сумме: {count_of_bit + count_of_combination + len(code_cx1)}")
    # print(array_code)

    array_count_len = []
    for i in array_code:
        array_count_len.append(len(i))

    array_regular_code = []

    n = max_len_for_vertelex - 1
    res = []

    """Просчитываем все возможные комбинации"""
    for i in range(2**n):
        s = ""
        for j in range(n):
            s = str(i%2) + s
            i = i//2
        res.append(s)

    # print(res)
    #print(array_count_len)

    # массив для подсчета кол-ва встречающихся длин
    array_count_of_count_of_len = []

    for i in array_count_len:
        if i not in array_count_of_count_of_len:
            array_count_of_count_of_len.append(i)

    #print(array_count_of_count_of_len)

    # собираем комбинации нужные
    for i in range(len(array_count_of_count_of_len)):
        n = array_count_len.count(array_count_of_count_of_len[i])
        count = 0

        for k in res:
            if count == n:
                break;
            c_buf = 0
            code = k[:array_count_of_count_of_len[i]]
            for j in array_regular_code:
                if not code.startswith(j): #j not in code:
                    c_buf += 1
            if code not in array_regular_code and c_buf == len(array_regular_code):
                array_regular_code.append(code)
                count += 1
    code_new = ''
    for i in line:
        code_new += array_regular_code[array_char.index(i)]
    print(f"c(x2)={code_new}")
    # print(len(array_regular_code))
    #print(array_regular_code)
    # print(len(array_cheat))
    # print(array_cheat)
array_set(N, line, 1)
