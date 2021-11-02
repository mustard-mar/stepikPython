d = {}
maxcl = 1
with open("input.txt") as input:
    while True:
        minil = input.readline().split("\t")
        if minil==[""]:break
        cl = int(minil[0])
        if cl not in d: d[cl] = [0,0]
        d[cl][0]+=int(minil[2])
        d[cl][1]+=1
        if cl>maxcl: maxcl=cl
for i in range(maxcl+1):
    if i in d: print(i,d[i][0]/d[i][1])
    else: print(i,"-")
