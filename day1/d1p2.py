increase = 0
scanwindow = 3
fn = 'sonar.txt'
f = open(fn, 'r')
sonars = f.readlines()

i = 0
while i+scanwindow < len(sonars):
    sum1 = 0
    sum2 = 0
    for j in range(scanwindow):
        sum1 = sum1 + int(sonars[i+j])
        sum2 = sum2 + int(sonars[i+j+1])
    if sum1 < sum2:
        increase = increase+1
    i = i+1
print("increase: "+str(increase))