import heapq
from collections import namedtuple
#line = "abc"
#line = 'НЕ ИМЕЙ СТО РУБЛЕЙ, А ИМЕЙ СТО ДРУЗЕЙ.'
#line = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."
N = len(line)

def make_bytes(text:str, encoding = 'cp1251') -> str:
    return ''.join(bin(c)[2:].rjust(8, '0') for c in text.encode(encoding))

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encode(dict_h):
    hheapq = []

    for char, count_char in dict_h.items():
        hheapq.append((count_char, len(hheapq), Leaf(char)))

    heapq.heapify(hheapq)
    count = len(hheapq)

    while len(hheapq) > 1:
        count_char_1, _count1, left = heapq.heappop(hheapq)
        count_char_2, _count2, right = heapq.heappop(hheapq)

        heapq.heappush(hheapq, (count_char_1 + count_char_2, count, Node(left, right)))

        count += 1

    code = {}

    if hheapq:
        [(count_char, _count, root)] = hheapq
        root.walk(code, "")

    return code

def array_set(N, line, c):

    array_set = []
    dictionary = {}

    if c == 1:
        for i in range(N):
            if line[i] not in array_set:
                array_set.append(line[i])

        for i in array_set:
            dictionary[i] = line.count(i)

    code = huffman_encode(dictionary)
    text = ''
    for i in line:
        text += code[i]

    array_code = []
    array_char = []

    for char in sorted(code):
        array_code.append(code[char])
        array_char.append(char)

    for i in range(len(array_code)):
        for j in range(len(array_code)-1):
            if len(array_code[j]) > len(array_code[j+1]):
                array_code[j], array_code[j+1] = array_code[j+1], array_code[j]
                array_char[j], array_char[j+1] = array_char[j+1], array_char[j]

    array_cx1 = []

    for code in array_code:
        new_code = ''
        for i in range(len(code)):
            new_code += '0'
        new_code += '1'
        array_cx1.append(new_code)

    #print(array_code)
    #print(array_cx1)
    code_cx1 = ""
    array_min = []
    for id in range(len(array_cx1[len(array_cx1)-1])):
        count = 0
        count_min = 0
        for cod in array_cx1:
            if len(cod) >= id:
                if len(cod) == id:
                    count += 1
                    code_cx1+= '1'
            else:
                count_min += 1

        if (id + 1 != len(array_cx1[len(array_cx1)-1])):
            code_cx1 += '0'*((2**id) - count - count_min*2*2*2*2)

    code_cx2 = ''
    for i in array_char:
        code_cx2 += make_bytes(i)
    print(len(code_cx1) + len(code_cx2))
array_set(N, line, 1)
