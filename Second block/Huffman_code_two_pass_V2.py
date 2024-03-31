def Frequency(text, text_set):# создание словаря вероятностей для любого кол-ва символов
    result = dict()
    for i in text_set:
        result[i] = text.count(i)/(len(text) - (len(i) - 1))
    return result


def PrintHuff(my_text, haffman_buff, haffman_service_buff):# печать

    c1 = ""
    c2 = ""

    print("c1(x) = ", end = '')
    print(haffman_service_buff, end = "")
    c1 += haffman_service_buff

    my_string = ''.join(haffman_buff.keys())
    ascii_string = ''.join(bin(c)[2:].rjust(8, '0') for c in my_string.encode('cp1251'))
    print(ascii_string)

    c1 += ascii_string

    print()
    print("c2(x) = ", end = '')
    for i in my_text:
        code = haffman_buff.get(i)
        print(code, end="")
        c2 += code

    print(end= "\n\n")

    print("c(x) = ", c1, c2, sep="")

    print()

    print("l1(x) = ", len(c1))
    print("l2(x) = ", len(c2))
    print("l(x) = l1(x) + l2(x) = ", len(c1) + len(c2))

def build_string_from_tree(root):
    if root is None:
        return ""
    if root.lchild is None and root.rchild is None:
        return "1"
    return "0" + build_string_from_tree(root.lchild) + build_string_from_tree(root.rchild)


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

if __name__=='__main__':
    my_text = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."
    #my_text = "НЕ ИМЕЙ СТО РУБЛЕЙ, А ИМЕЙ СТО ДРУЗЕЙ."
    text_buff  = my_text.split(' ')
    my_text = "_".join(text_buff)


    text_set = sorted(set(my_text), key=my_text.index)

    frequency_dict_1 = Frequency(my_text, text_set)

    tree = HuffmanTree(frequency_dict_1)
    result = dict()

    serviceResult = build_string_from_tree(tree.root)
    print(serviceResult)
    tree.Hu_generate(tree.root, 0 ,result)

    PrintHuff(my_text, result, serviceResult)
