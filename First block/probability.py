line = "И тридцать витязей прекрасных чредой из вод выходят ясных, и с ними дядька их морской.\nИ вот нашли большое поле: есть разгуляться где на воле! Построили редут."

N = len(line)

print()
array_set = set()

for i in line:
    array_set.add(i)

id = 1

print('  i      xi        Ni    P(xi)')
print('_______________________________')
print()

for i in array_set:
    
    if i != '\n':
        print(f"{id:3}      {i:3}     {line.count(i):3}     {line.count(i)/N:.4f}")
    else:
        print(f"{id:3}      \\n      {line.count(i):3}     {line.count(i)/N:.4f}")
    id += 1

array_set = set()

N -= 1

id = 1

for i in range(N):
    array_set.add(line[i]+line[i+1])
print()
print('  i      xi         Ni     P(xi)')
print('_______________________________')
print()

for i in array_set:
    
    if '\n' not in i:
        print(f"{id:3}      {i:4}     {line.count(i):3}     {line.count(i)/N:.4f}")
    else:
        bufi = i[1-i.find('\n')]
        if i.find('\n') == 1:
            print(f"{id:3}      {bufi}\\n      {line.count(i):3}     {line.count(i)/N:.4f}")
        else:
            print(f"{id:3}      \\n{bufi}      {line.count(i):3}     {line.count(i)/N:.4f}")
    id += 1

array_set = set()

N -= 1

id = 1

for i in range(N):
    array_set.add(line[i]+line[i+1]+line[i+2])

print()
print('  i       xi         Ni     P(xi)')
print('_______________________________')
print()

for i in array_set:

    if '\n' not in i:
        print(f"{id:3}      {i:5}     {line.count(i):3}     {line.count(i)/N:.4f}")
    else:
        if i.find('\n') == 1:
            print(f"{id:3}      {i[0]}\\n{i[2]}      {line.count(i):3}     {line.count(i)/N:.4f}")
        elif i.find('\n') == 0:
            print(f"{id:3}      \\n{i[1]}{i[2]}      {line.count(i):3}     {line.count(i)/N:.4f}")
        else:
            print(f"{id:3}      {i[0]}{i[1]}\\n      {line.count(i):3}     {line.count(i)/N:.4f}")
    id += 1