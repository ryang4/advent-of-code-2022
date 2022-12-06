def openFile(filename):

    f = open(filename, 'r')
    result = f.readlines()
    f.close()

    return result


def getUpperPriority(c):
    return ord(c) - 38


def getLowerPriority(c):
    return ord(c) - 96


def getPriority(c):
    print(c)
    if c.isupper():
        return getUpperPriority(c)
    return getLowerPriority(c)


def getDuplicates(c1, c2):
    c1Items = set()

    for item in c1:
        c1Items.add(item)

    for item in c2:
        if item in c1Items:
            return item


def calcPriorities(input):

    prioritySum = 0

    for line in input:

        middle = len(line) // 2

        c1 = line[:middle]
        c2 = line[middle:]
        dupeItem = getDuplicates(c1, c2)

        prioritySum += getPriority(dupeItem)

    return prioritySum


def calcBadgePriority(group):
    itemSet = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
    for item in itemSet:
        return getPriority(item)


def getGroups(input):

    group = []

    prioritySum = 0

    for line in input:
        lineList = [item for item in line.strip()]
        group.append(lineList)
        if len(group) == 3:
            prioritySum += calcBadgePriority(group)
            group = []
    
    return prioritySum


print(calcPriorities(openFile('input.txt')))
print(getGroups(openFile('input.txt')))
