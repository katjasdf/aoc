import re

lines = open('data.txt', 'r').readlines()

def first_part():
    numbers = []
    response = 0

    for line in lines:
        line_numbers = []
        for letter in line:
            if letter.isnumeric():
                line_numbers.append(letter)

        two_numbers = line_numbers[0] + line_numbers[-1]
        numbers.append(two_numbers)

    for number in numbers:
        response += int(number)

    print(response)

def second_part():
    written_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = []
    response = 0

    for line in lines:
        line_numbers = []
        for i, letter in enumerate(line, start=1):
            if letter.isnumeric():
                line_numbers.append((letter, i))
        
        for i, written_number in enumerate(written_numbers, start=1):
            all_matches = re.finditer(written_number, line)
            
            for match in all_matches:
                matches = str(i), match.start()
                line_numbers.append(matches)
        
        sorted_numbers = sorted(line_numbers, key=lambda x: x[1])

        two_numbers = sorted_numbers[0][0] + sorted_numbers[-1][0]
        numbers.append(two_numbers)
    
    for number in numbers:
        response += int(number)

    print(response)

first_part()
second_part()