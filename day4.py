import numpy as np
with open('day4.txt', 'r') as inputFile:
    lines = [line.strip() for line in list(inputFile)]

rows = len(lines)
cols = len(lines[0])
data = ''.join(lines)

wordsearch = np.array(list(data), dtype=np.dtype(str))
wordsearch = np.reshape(wordsearch, (rows, cols))
wordsearch = np.pad(wordsearch, 4, constant_values='o')
rows, cols = np.shape(wordsearch)

xmasArray = [
    ['S', ' ', ' ', 'S', ' ', ' ', 'S'],
    [' ', 'A', ' ', 'A', ' ', 'A', ' '],
    [' ', ' ', 'M', 'M', 'M', ' ', ' '],
    ['S', 'A', 'M', 'X', 'M', 'A', 'S'],
    [' ', ' ', 'M', 'M', 'M', ' ', ' '],
    [' ', 'A', ' ', 'A', ' ', 'A', ' '],
    ['S', ' ', ' ', 'S', ' ', ' ', 'S'],
]

xmas = np.array(xmasArray, dtype = np.dtype(str))
xcount = 0
for x in range(4, rows - 4):
    for y in range(4, cols - 4):
        if wordsearch[x, y] != 'X':
            continue
        chunk = wordsearch[x - 3:x + 4, y - 3:y + 4]
        compare = chunk == xmas

        if np.sum(compare[0:4, 3]) == 4: #up
            xcount += 1

        if np.sum(compare[3:7, 3]) == 4: #down
            xcount += 1

        if np.sum(compare[3, 3:7]) == 4: #right
            xcount += 1

        if np.sum(compare[3, 0:4]) == 4: #left
            xcount += 1

        if np.trace(compare[0:4, 0:4]) == 4: #ul
            xcount += 1

        if np.trace(np.fliplr(compare[0:4, 3:7])) == 4: #ur
            xcount += 1

        if np.trace(np.fliplr(compare[3:7, 0:4])) == 4: #dl
            xcount += 1

        if np.trace(compare[3:7, 3:7]) == 4: #dr
            xcount += 1


print(f'part 1: {xcount}')

ycount = 0
for x in range(4, rows - 4):
    for y in range(4, cols - 4):
        if wordsearch[x, y] != 'A':
            continue

        chunk = wordsearch[x - 1:x + 2, y - 1:y + 2]

        if chunk[0,0] == 'M' and chunk[2,2] == 'S':
            if chunk[0, 2] == 'M' and chunk[2,0]== 'S':
                ycount += 1
            if chunk[0, 2] == 'S' and chunk[2,0]== 'M':
                ycount += 1

        if chunk[0,0] == 'S' and chunk[2,2] == 'M':
            if chunk[0, 2] == 'M' and chunk[2,0]== 'S':
                ycount += 1
            if chunk[0, 2] == 'S' and chunk[2,0]== 'M':
                ycount += 1

print(f'part 2: {ycount}')
