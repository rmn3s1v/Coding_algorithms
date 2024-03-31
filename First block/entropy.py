from math import *
line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."

N = len(line)

print()
array_set = set()

for i in line:
    array_set.add(i)

id = 1

print('_________________________________________________________')
print()
print('  i      xi        Ni    P(xi)       I(xi)   p(xi)*I(xi)')
print('_________________________________________________________')
print()

count_1 = 0

for i in array_set:
    
    if i != '\n':
        print(f"{id:3}      {i:3}     {line.count(i):3}     {line.count(i)/N:.4f}     {abs(log2(line.count(i)/N)):.4f}     {(line.count(i)/N*abs(log2(line.count(i)/N))):.4f}")
    else:
        print(f"{id:3}      \\n      {line.count(i):3}     {line.count(i)/N:.4f}     {abs(log2(line.count(i)/N)):.4f}     {(line.count(i)/N*abs(log2(line.count(i)/N))):.4f}")
    id += 1

    count_1 += line.count(i)/N*abs(log2(line.count(i)/N))

print(f"\nH(x^1) = {count_1:.4f}")
print(f"H1(x) = {count_1/1:.4f}")
print(f"H(x|x^0) = {count_1:.4f}")

array_set = set()

N -= 1

id = 1

for i in range(N):
    array_set.add(line[i]+line[i+1])
print()
print('__________________________________________________________')
print()
print('  i      xi         Ni     P(xi)     I(xi)    p(xi)*I(xi)')
print('__________________________________________________________')
print()

count_2 = 0

for i in array_set:
    
    if '\n' not in i:
        print(f"{id:3}      {i:4}     {line.count(i):3}     {line.count(i)/N:.4f}     {abs(log2(line.count(i)/N)):.4}     {line.count(i)/N*abs(log2(line.count(i)/N)):.4f}")
    else:
        bufi = i[1-i.find('\n')]
        if i.find('\n') == 1:
            print(f"{id:3}      {bufi}\\n      {line.count(i):3}     {line.count(i)/N:.4f}     {abs(log2(line.count(i)/N)):.4f}    {line.count(i)/N*abs(log2(line.count(i)/N)):.4f}")
        else:
            print(f"{id:3}      \\n{bufi}      {line.count(i):3}     {line.count(i)/N:.4f}     {abs(log2(line.count(i)/N)):.4f}    {line.count(i)/N*abs(log2(line.count(i)/N)):.4f}")
    id += 1
    count_2 += line.count(i)/N*abs(log2(line.count(i)/N))

print(f"\nH(x^2) = {count_2:.4f}")
print(f"H2(x) = {count_2/2:.4f}")
print(f"H(x|x^1) = {count_2 - count_1:.4f}")

array_set = set()

N -= 1

id = 1

for i in range(N):
    array_set.add(line[i]+line[i+1]+line[i+2])

print()
print('__________________________________________________________')
print()
print('  i       xi         Ni     P(xi)     I(xi)    p(xi)*I(xi)')
print('__________________________________________________________')
print()

count_3 = 0

for i in array_set:

    if '\n' not in i:
        print(f"{id:3}      {i:5}     {line.count(i):3}     {line.count(i)/N:.4f}     {abs(log2(line.count(i)/N)):.4f}     {line.count(i)/N*abs(log2(line.count(i)/N)):.4f}")
    else:
        if i.find('\n') == 1:
            print(f"{id:3}      {i[0]}\\n{i[2]}      {line.count(i):3}     {line.count(i)/N:.4f}     {(abs(log2(line.count(i)/N))):.4f}     {(line.count(i)/N*abs(log2(line.count(i)/N))):.4f}")
        elif i.find('\n') == 0:
            print(f"{id:3}      \\n{i[1]}{i[2]}      {line.count(i):3}     {line.count(i)/N:.4f}     {(abs(log2(line.count(i)/N))):.4f}     {(line.count(i)/N*abs(log2(line.count(i)/N))):.4f}")
        else:
            print(f"{id:3}      {i[0]}{i[1]}\\n      {line.count(i):3}     {line.count(i)/N:.4f}     {(abs(log2(line.count(i)/N))):.4f}     {(line.count(i)/N*abs(log2(line.count(i)/N))):.4f}")
    id += 1

    count_3 += line.count(i)/N*abs(log2(line.count(i)/N))

print(f"\nH(x^3) = {count_3:.4f}")
print(f"H3(x) = {count_3/3:.4f}")
print(f"H(x|x^2) = {count_3 - count_1 - (count_2 - count_1):.4f}")