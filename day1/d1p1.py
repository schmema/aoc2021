increase = 0

fn = 'sonar.txt'
f = open(fn, 'r')
sonars = f.readlines()

i = 0
while i+1 < len(sonars):
    if int(sonars[i+1]) > int(sonars[i]):
        increase = increase+1
    i = i+1
print("increase: "+str(increase))