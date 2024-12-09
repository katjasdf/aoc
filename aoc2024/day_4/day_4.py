import re

lines = open('data.txt').readlines()
linesGrid = ([lines.split() for lines in lines])

result = 0
lettersGrid = []

for array in linesGrid:
    letters = []
    for line in array:
        match = re.findall(r'(?=(XMAS|SAMX))', line)
        result += len(match)

        for letter in line:
            letters.append(letter)

    lettersGrid.append(letters)

verticalArray = list(zip(*lettersGrid))

for array in verticalArray:
    verticalLine = ''.join(array)
    match = re.findall(r'(?=(XMAS|SAMX))', verticalLine)
    result += len(match)

n, m = len(lettersGrid), len(lettersGrid[0])
diagonalsArray = []

for i in range(n):
    diagonals = []
    for k in range(min(n - i, m)):
        diagonals.append(lettersGrid[i + k][k])

    diagonalsArray.append(diagonals)

for i in range(1, m):
    diagonals = []
    for k in range(min(m - i, n)):
        diagonals.append(lettersGrid[k][i + k])

    diagonalsArray.append(diagonals)

for i in range(m - 1, -1, -1):
    diagonals = []
    for k in range(min(n, i + 1)):
        diagonals.append(lettersGrid[k][i - k])

    diagonalsArray.append(diagonals)

for i in range(1, n):
    diagonals = []
    for k in range(min(n - i, m)):
        diagonals.append(lettersGrid[i + k][m - 1 - k])

    diagonalsArray.append(diagonals)

for diagonal in diagonalsArray:
    diagonalLine = ''.join(diagonal)
    match = re.findall(r'(?=(XMAS|SAMX))', diagonalLine)
    result += len(match)

print(result)
