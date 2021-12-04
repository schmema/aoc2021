import time
fn = 'input.txt'
f = open(fn, 'r')


with f as openfile:
    numberlist = f.readline().split(',')
    f.readline()
    k = 0
    bingocharts = [[]]
    for line in openfile:
        if line == "\n":
            bingocharts.append([])
            k = k+1
        else:
            bingocharts[k].append(line.split())

winlist = [[[0]*5 for i in range(5)]for i in range(len(bingocharts))]

def winchecker(winchart,bingochart):
    modes = ["reg","trans"]
    for mode in modes:
        if mode =="trans":
            winchart = list(map(list, zip(*winchart)))
            bingochart = list(map(list, zip(*bingochart)))
        for y in range(5):
            for x in range(5):
                if sum(winchart[y])== 5:
                    return(True, bingochart, winchart)
    return False,[], []
win = False
for number in numberlist:
    for chart in range(len(bingocharts)):
        for y in range(5):
            for x in range(5):
                if int(number) == int(bingocharts[chart][y][x]):
                    winlist[chart][y][x] = 1
                    win,winningchart, checklist = winchecker(winlist[chart],bingocharts[chart])
                    if win:
                        print("BINGO!")
                        print(*checklist,sep='\n')
                        print(*winningchart,sep='\n')
                        winsum = 0
                        for i in range(len(winningchart)):
                            for x in range(5):
                                if checklist[i][x] == 0:
                                    winsum = winsum + int(winningchart[i][x])
                        print(str(winsum)+ " * "+number+ " = "+str(winsum*int(number)))
                        break
            if win:
                break
        if win:
            break
    if win:
        break
