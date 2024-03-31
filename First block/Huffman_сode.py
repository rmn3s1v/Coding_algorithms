from prettytable import PrettyTable
import heapq
from collections import namedtuple

# line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."
line = "там королевич мимоходом пленяет грозного царя. у наших ушки на макушке! чуть утро осветило пушки и леса синие верхушки - французы тут как тут."

N = len(line)

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

    array_set = set()
    dictionary = {}

    if c == 1:
        for i in range(N):
            array_set.add(line[i])

        for i in array_set:
            dictionary[i] = line.count(i)

    elif c == 2:
        for i in range(N):
            array_set.add(line[i] + line[i+1])

        for i in array_set:
            dictionary[i] = line.count(i)

    else:
        for i in range(N):
            array_set.add(line[i] + line[i+1] + line[i+2])

        for i in array_set:
            dictionary[i] = line.count(i)

    id = 1
    code = huffman_encode(dictionary)

    mytable = PrettyTable()
    mytable.field_names = ["i", "Xi", "Pi", "Ci", "Li"]
    L_mid = 0

    if c == 1:
        for char in sorted(code):
            if char == '\n':
                mytable.add_row([id, '\\n', round(line.count(char)/N, 4), code[char], len(code[char])])
            else:
                mytable.add_row([id, char, round(line.count(char)/N, 4), code[char], len(code[char])])

            id += 1
            L_mid += len(code[char])*round(line.count(char)/N, 4)

        table1 = mytable.get_string(fields = ["i", "Xi", "Pi", "Ci", "Li"])
        print(table1)
        print(f"L^n/huf = {L_mid:.4f}")
        print(f"R^n/huf = {L_mid/1:.4f}")
        print()

    elif c == 2:
        for char in sorted(code):
            if '\n' not in char:
                mytable.add_row([id, char, round(line.count(char)/N, 4), code[char], len(code[char])])
            else:
                buf_char = char.replace('\n', '\\n')
                mytable.add_row([id, buf_char, round(line.count(char)/N, 4), code[char], len(code[char])])

            id += 1
            L_mid += len(code[char])*round(line.count(char)/N, 4)

        table1 = mytable.get_string(fields = ["i", "Xi", "Pi", "Ci", "Li"])
        print(table1)
        print(f"L^n/huf = {L_mid:.4f}")
        print(f"R^n/huf = {L_mid/2:.4f}")
        print()

    else:
        for char in sorted(code):
            if '\n' not in char:
                mytable.add_row([id, char, round(line.count(char)/N, 4), code[char], len(code[char])])
            else:
                buf_char = char.replace('\n', '\\n')
                mytable.add_row([id, buf_char, round(line.count(char)/N, 4), code[char], len(code[char])])

            id += 1
            L_mid += len(code[char])*round(line.count(char)/N, 4)

        table1 = mytable.get_string(fields = ["i", "Xi", "Pi", "Ci", "Li"])
        print(table1)
        print(f"L^n/huf = {L_mid:.4f}")
        print(f"R^n/huf = {L_mid/3:.4f}")
        print()


array_set(N, line, 1)
array_set(N-1, line, 2)
array_set(N-2, line, 3)
