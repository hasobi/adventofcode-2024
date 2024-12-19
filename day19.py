from functools import cache

DesignList = []
InputState = 0
with open("day19.txt", "r") as data:
    for t in data:
        Line = t.strip()
        if Line == "":
            InputState = 1
        elif InputState == 0:
            TowelSet = set(Line.split(", "))
        elif InputState == 1:
            DesignList.append(Line)

MaxTowelLength = 0
for t in TowelSet:
    MaxTowelLength = max(MaxTowelLength, len(t))


def DesignPossible(Design, MaxLen):
    Queue = [Design]
    while Queue:
        SubDesign = Queue.pop()
        if SubDesign in TowelSet:
            return True
        Max = min(MaxLen, len(SubDesign))
        for y in range(1,Max+1):
            if SubDesign[0:y] in TowelSet:
                Queue.append(SubDesign[0:y])
    
    return False

Part1Answer = 0
for v in reversed(range(len(DesignList))):
    Design = DesignList[v]
    if DesignPossible(Design, MaxTowelLength):
        Part1Answer += 1
    else:
        del DesignList[v]

@cache
def DesignCombos(Design, MaxLen):
    Max = min(MaxLen, len(Design))
    Combos = 0
    if Design in TowelSet:
        Combos += 1
    for y in range(1,Max+1):
        if Design[0:y] in TowelSet:
            Combos += DesignCombos(Design[y:], MaxLen)
    return Combos

Part2Answer = 0
for d in DesignList:
    Part2Answer += DesignCombos(d, MaxTowelLength)

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
