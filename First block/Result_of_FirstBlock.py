from math import *

line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\n И вот нашли большое поле: есть разгуляться где на воле! Построили редут."

def Code(line, cycle):

    N = len(line)

    if N % 6 != 0:
        while N % 6 != 0:
            N += 1
            line += ' '
    
    char_array = []
    pxi_array = []
    qi_array = []

    if cycle == 1:
        for i in line:
            if i not in char_array:
                char_array.append(i)
    
    if cycle == 2:
        for i in range(len(line)-1):
            if line[i]+line[i+1] not in char_array:
                char_array.append(line[i]+line[i+1])

    if cycle == 3:
        for i in range(len(line)-2):
            if line[i]+line[i+1] not in char_array:
                char_array.append(line[i]+line[i+1]+line[i+2])
    
    #print(char_array)

    for i in char_array:
        pxi_array.append(line.count(i)/N)

    for i in range(0, len(pxi_array)):
        count = 0
        for j in range(i):
            count += pxi_array[j]
        qi_array.append(count)
    
    code = ""
    #print(qi_array)
    R = 0
    cR = 0

    if cycle == 1:
        for i in range(0, N, 6):
            F = 0
            G = 1
            for j in range(i, i+6):
                F = F + qi_array[char_array.index(line[j])]*G
                G = G * pxi_array[char_array.index(line[j])]
            l = ceil(-log2(G))+1
            c = 0
            number = F + G/2
            code_buf = ''
            while c != l:
                if (number >= 1): number-=1
                code_buf += str(floor(number*2%10))
                number *= 2
                c += 1
            code += code_buf
            R += l/6
            cR += 1

    if cycle == 2:
        for i in range(0, N, 6):
            F = 0
            G = 1
            for j in range(i, i+6, 2):
                F = F + qi_array[char_array.index(line[j]+line[j+1])]*G
                G = G * pxi_array[char_array.index(line[j]+line[j+1])]
            l = ceil(-log2(G))+1
            c = 0
            number = F + G/2
            code_buf = ''
            while c != l:
                if (number >= 1): number-=1
                code_buf += str(floor(number*2%10))
                number *= 2
                c += 1
            code += code_buf
            R += len(code_buf)/6
            cR += 1

    if cycle == 3:
        for i in range(0, N, 6):
            F = 0
            G = 1
            for j in range(i, i+6, 3):
                F = F + qi_array[char_array.index(line[j]+line[j+1]+line[j+2])]*G
                G = G * pxi_array[char_array.index(line[j]+line[j+1]+line[j+2])]
            l = ceil(-log2(G))+1
            c = 0
            number = F + G/2
            code_buf = ''
            while c != l:
                if (number >= 1): number-=1
                code_buf += str(floor(number*2%10))
                number *= 2
                c += 1
            code += code_buf
            R += len(code_buf)/6
            cR += 1

    print(code)
    print(len(code))
    print(f"{len(code)/cR:0.4f}")
    print(f"{R/cR:0.4f}")
    print()

Code(line, 1)
Code(line, 2)
Code(line, 3)
