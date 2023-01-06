path = "./data.csv"

def writeFile(path):
    file = open(path, 'w', encoding='utf-8')
    for i in range(10):
        file.write("value {0} = {1}\n".format(i+1, i))
    file.close()

def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        print(line)
    file.close()

writeFile(path)
readFile(path)