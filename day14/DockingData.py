with open('test.txt') as file:
    data=[l.strip().replace(' = ',' ') for l in file.readlines()]