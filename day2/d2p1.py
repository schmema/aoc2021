fn = 'directions.txt'
f = open(fn, 'r')

directions = {'horizontal': 0,'vertical': 0}
with f as openfile:
    for line in openfile:
        (command, val) = line.split()
        if command == 'forward':
            directions['horizontal'] = directions['horizontal'] + int(val)
        elif command == 'down':
            directions['vertical'] = directions['vertical'] + int(val)
        elif command == 'up':
            directions['vertical'] = directions['vertical'] - int(val)
print(str(directions) + ' ' + str(directions['horizontal']*directions['vertical']))