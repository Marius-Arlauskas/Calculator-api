def calculate(info):
    import re
    numbers = re.findall("\d+(?:\.\d+)?", info)
    if len(numbers) != 2:
        return 'Incorrect amount of NUMBER arguments, reenter your values from the start.'
    else:
        if sum([x in '+-/*x' for x in info]) != 1:
            return 'Incorrect amount of OPERAND arguments, reenter your values from the start.'
        else:
            result = 'I did not do my job, no idea why'
            if '+' in info:
                result = float(numbers[0]) + float(numbers[1])
            if '-' in info:
                result = float(numbers[0]) - float(numbers[1])
            if '/' in info:
                result = float(numbers[0]) / float(numbers[1])
            if '*' in info or 'x' in info:
                result = float(numbers[0]) * float(numbers[1])
            return str(result)
