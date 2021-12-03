import time 

fn = 'input.txt'
f = open(fn, 'r')

#bitcounter = [[0 for c in range(2)] for r in range(len(str(f.readline()).rstrip()))]
inputlist = f.readlines()

def run_bitcounter(inputlist):
    bitcounter = [[0 for c in range(2)] for r in range(12)]
    gammarate = ""
    epsilonrate=""
    for line in inputlist:
        line = line.rstrip()
        for i in range(len(line)):
            if int(line[i]) == 0:
                bitcounter[i][0] = bitcounter[i][0] + 1
            elif int(line[i]) ==1:
                bitcounter[i][1] = bitcounter[i][1] + 1
    #print(bitcounter)
    for i in range(len(bitcounter)):
        if bitcounter[i][0] < bitcounter[i][1]:
            gammarate = gammarate + str(1)
            epsilonrate = epsilonrate + str(0)
        elif bitcounter[i][0] > bitcounter[i][1]:
            gammarate = gammarate + str(0)
            epsilonrate = epsilonrate + str(1)
        else:
            gammarate = gammarate + str(1)
            epsilonrate = epsilonrate + str(0)
    return(gammarate, epsilonrate)



grate,erate = run_bitcounter(inputlist)

print(grate + ' ' + str(int(grate,2))+"\n"\
    +erate + ' ' + str(int(erate,2))+"\n"\
    +str(int(erate,2)*int(grate,2)))

#p2
runlist = ["oxi","co2"]

lsr = {'oxirate':0,'corate':0}

for run in runlist:
    print("\n")
    fn = 'input.txt'
    f = open(fn, 'r')
    inputlist = f.readlines()
    poplist = []

    for i in range(12):
        poplist.sort(reverse=True)
        for p in poplist:
            inputlist.pop(p)
        poplist = []
        if len(inputlist) >1:
            grate,erate = run_bitcounter(inputlist)
            if run == "oxi":
                print(grate[i])
                for j in range(len(inputlist)):
                    if int(inputlist[j][i]) != int(grate[i]):
                        poplist.append(j)
            if run == "co2":
                print(erate[i])
                for j in range(len(inputlist)):
                    if int(inputlist[j][i]) != int(erate[i]):
                        poplist.append(j)
    if run == "oxi":
        lsr['oxirate'] = str(inputlist[0]).rstrip()
    elif run == "co2":
        lsr['corate'] = str(inputlist[0]).rstrip()
        
    
print (str(lsr) + "\n" \
    + str(int(str(lsr['oxirate']),2))+" "+str(int(str(lsr['corate']),2))+ "\n"\
    +   str(int(str(lsr['oxirate']),2)*int(str(lsr['corate']),2)))

