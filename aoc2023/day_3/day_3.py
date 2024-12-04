import re

lines = open('data.txt', 'r').readlines()

for i, line in enumerate(lines, start=1):
    numbers = re.finditer(r'\d+', line)
    #for number in numbers:
    #    print(i, number.group(), number.span())

for i, line in enumerate(lines, start=1):
    special_characters = re.finditer(r'[\W][^\.]', line)
    for special_character in special_characters:
        print(i, special_character.group(), special_character.span())