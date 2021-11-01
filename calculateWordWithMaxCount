l = []
mini = []
d = {"":0}
with open("input.txt") as input:
    while True:
        mini = input.readline().lower().strip().split()
        if mini==[]: break
        l += mini
        print(mini)
for i in l:
    if(i not in d):d[i] = 0
    d[i]+=1
maxlist = {}
maxkey = ""
for key in d:
    if d[key] > d[maxkey]:
        maxkey = key
    if d[key] == d[maxkey] and key!=maxkey and key < maxkey:
        maxkey = key
print(maxkey,d[maxkey])
