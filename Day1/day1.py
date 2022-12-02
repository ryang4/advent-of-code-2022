def openFile(filename):
    
    f = open(filename, 'r')
    result = f.readlines()
    f.close()

    return result

def singleSum(input):
    currentElfSum = 0
    maxElfSum = 0
    for line in input:
        if len(line.strip()) != 0:
            currentElfSum += int(line.strip())
        else:
            maxElfSum = max(currentElfSum, maxElfSum)
            currentElfSum = 0
    
    return maxElfSum

def xSum(input, x):
    currentElfSum = 0
    elfSums = []
    for line in input:
        if len(line.strip()) != 0:
            currentElfSum += int(line.strip())
        else:
            elfSums.append(currentElfSum)
            currentElfSum = 0
    
    elfSums = sorted(elfSums)
    
    return elfSums[-x:]


def main():
    input = openFile('input.txt')
    maxElfSum = xSum(input, 3)

    print(sum(maxElfSum))

main()
    

