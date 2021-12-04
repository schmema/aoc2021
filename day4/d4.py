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

winlist = [[[0]*len(bingocharts[0][0]) for i in range(len(bingocharts[0]))]for i in range(len(bingocharts))]

def winchecker(winchart,bingochart):
    modes = ["reg","trans"]
    for mode in modes:
        if mode =="trans":
            winchart = list(map(list, zip(*winchart)))
            bingochart = list(map(list, zip(*bingochart)))
        for y in range(len(winchart)):
            for x in range(len(winchart[y])):
                if sum(winchart[y])== len(winchart[y]):
                    return(True, bingochart, winchart)
    return False,[], []

win = False

donecharts = []
for number in numberlist:
    for chart in range(len(bingocharts)):
        if (len(donecharts) == len(bingocharts)):
            break
        if chart not in donecharts:
            for y in range(len(bingocharts[chart])):
                for x in range(len(bingocharts[chart][y])):
                    if int(number) == int(bingocharts[chart][y][x]):
                        winlist[chart][y][x] = 1
                        win,winningchart, checklist = winchecker(winlist[chart],bingocharts[chart])
                        if win:
                            win = False
                            donecharts.append(chart)
                            if (len(donecharts) == 1) or (len(donecharts)==len(bingocharts)):
                                print(str(len(donecharts))+". BINGO!")
                                print(*checklist,sep='\n')
                                print(*winningchart,sep='\n')
                                winsum = 0
                                for i in range(len(winningchart)):
                                    for x in range(len(winningchart[i])):
                                        if checklist[i][x] == 0:
                                            winsum = winsum + int(winningchart[i][x])
                                print(str(winsum)+ " * "+number+ " = "+str(winsum*int(number))+"\n")
                            
