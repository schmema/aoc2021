fn = 'directions.txt'
f = open(fn, 'r')

directions = {'horizontal': 0,'vertical': 0, 'aim': 0}
with f as openfile:
    for line in openfile:
        (command, val) = line.split()
        if command == 'forward':
            directions['horizontal'] = directions['horizontal'] + int(val)
            directions['vertical'] = directions['vertical'] + int(val)*directions['aim']
        elif command == 'down':
            directions['aim'] = directions['aim'] + int(val)
        elif command == 'up':
            directions['aim'] = directions['aim'] - int(val)
print(str(directions) + ' ' + str(directions['horizontal']*directions['vertical']))