line = ''
with open("input.txt") as input:
    line = input.readline().strip()
size = len(line)
newline = ''
i = 0
while i < size:
    letter = line[i]
    i+=1
    numbline = ''
    while i<size and ord("0")<=ord(line[i])<=ord("9") :
        numbline+=line[i]
        i+=1
    print(numbline)
    numb = int(numbline)
    newline +=letter*numb
    with open("output.txt", "w") as output:
        output.write(newline)
