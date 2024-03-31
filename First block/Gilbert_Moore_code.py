from prettytable import PrettyTable 
from math import *
line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."
N = len(line)

def task(N, line, c):
    Lhn = 0
    Rnx = 0

    # таблица
    mytable = PrettyTable()
    mytable.field_names = ["i", "Xi", "Pi", "qi", "Sigi", "I(xi)", "li", "Ci"]

    set_Char1 = set()
    array_PxN1 = []
    array_Char1 = []
    array_Qi = [0.0000]
    array_Li = []
    array_Ci = []
    
    if c == 1:
        for i in range(N):
            set_Char1.add(line[i])

    elif c == 2:
        for i in range(N):
            set_Char1.add(line[i]+line[i+1])
    
    else:
        for i in range(N):
            set_Char1.add(line[i]+line[i+1]+line[i+2])

    # формируем вероятность символов
    for i in set_Char1:
        array_PxN1.append(line.count(i)/N)

    # формируем множество символов
    for i in set_Char1:
        array_Char1.append(i)

    if c == 1:
        for i in range(len(array_Char1)):
            if array_Char1[i] == '\n': array_Char1[i] = '\\n'
    
    else:
        for i in range(len(array_Char1)):
            if '\n' in  array_Char1[i]:
                buf_char = array_Char1[i]
                buf_char = buf_char.replace('\n', '\\n')
                array_Char1[i] = buf_char

    # считаем q вероятность
    array_Sigma = [round(array_Qi[0]+array_PxN1[0]/2, 4)]

    for i in range(1, len(array_PxN1)):
        count = 0
        for j in range(0, i):
            count += array_PxN1[j]
        array_Qi.append(round(count, 4))
        array_Sigma.append(round(count + array_PxN1[i]/2, 4)) 
        
    # формируем длину кода
    for i in array_PxN1:
        array_Li.append(ceil(abs(log2(i))+1))

    id = 0

    # формируем бинарный код
    for i in array_Sigma:
        buf_number = i
        count = 0
        code = ""
        while count != array_Li[id]:
            if (buf_number >= 1): buf_number -= 1
            code+= str(floor(buf_number*2%10))
            count += 1
            buf_number *= 2

        id += 1
        array_Ci.append(code)

    # формируем таблицу
    for i in range(len(array_PxN1)):
        mytable.add_row([i+1, array_Char1[i], round(array_PxN1[i], 4), array_Qi[i], array_Sigma[i], round(abs(log2(array_PxN1[i])),4), array_Li[i], array_Ci[i]])
    
    for i in range(len(array_Ci)):
        Lhn += (len(array_Ci[i])*round(array_PxN1[i], 4))

    print(mytable)
    print()
    print(f"L^n/F = {Lhn:.4f}")

    if c == 1:
        print(f"R^n/F = {Lhn/1:.4f}")

    elif c == 2:
        print(f"R^n/F = {Lhn/2:.4f}")

    else:
        print(f"R^n/F = {Lhn/3:.4f}")

    print()
   
task(N, line, 1)
task(N-1, line, 2)
task(N-2, line, 3)