import re
import math

lines = open('data.txt', 'r').readlines()

def first_part():
    class color:
        def __init__(self, color, max):
            self.color = color
            self.max = max

    games = lines
    response = 0
    red = color('red', 12)
    green = color('green', 13)
    blue = color('blue', 14)

    for c in [red, blue, green]:
        newlist = []
        for g in games:
            color_numbers = re.findall(r'(\d+\s)' + str(c.color), g)
            int_numbers = list(map(int, color_numbers))

            if max(int_numbers) <= c.max:
                newlist.append(g)

        games = newlist

    for game in games:
        game_number = re.match(r'Game\s\d+', game).group().split(' ')[1]
        response += int(game_number)

    print(response)

def second_part():
    games = lines
    response = 0

    for g in games:
        max_numbers = []
        for c in ['red', 'blue', 'green']:
            color_numbers = re.findall(r'(\d+\s)' + str(c), g)
            int_numbers = list(map(int, color_numbers))
            max_numbers.append(max(int_numbers))

        multiplied = math.prod(max_numbers)
        response += multiplied

    print(response)

first_part()
second_part()