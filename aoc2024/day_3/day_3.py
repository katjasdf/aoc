import re

data = open('data.txt').read()


def first_part():
    mul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', str(data))
    response = 0

    for m in mul:
        numbers = re.findall(r'\d{1,3}', m)
        response += int(numbers[0]) * int(numbers[1])

    print(response)


def second_part():
    response = 0
    enabled = True
    stop = False
    muls = []
    start = 0

    while stop is False:
        result = re.search(
            r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', str(data[start:]))

        if result is None:
            break

        mul = re.match(r'mul\(\d{1,3},\d{1,3}\)', str(result.group()))
        do = re.match(r'do\(\)', str(result.group()))
        dont = re.match(r'don\'t\(\)', str(result.group()))

        if mul is not None and enabled is True:
            start += result.end()
            muls.append(result)
        elif mul is not None and enabled is False:
            start += result.end()
        elif do is not None:
            start += result.end()
            enabled = True
        elif dont is not None:
            start += result.end()
            enabled = False
        else:
            stop = True

    for mul in muls:
        numbers = re.findall(r'\d{1,3}', mul.group())
        response += int(numbers[0]) * int(numbers[1])

    print(response)


first_part()
second_part()
