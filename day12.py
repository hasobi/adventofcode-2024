from collections import deque

InputList = []
with open("day12.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

CoordDict = {}
for y, f in enumerate(InputList):
    for x, c in enumerate(f):
        CoordDict[(x,y)] = c
        if c not in CoordDict:
            CoordDict[c] = set()
        CoordDict[c].add((x,y))

SkipSet = set()

def Region(SX, SY, Letter):
    Perimeter = 0
    ImperialCore = set()
    ImperialFrontier = deque()
    ImperialFrontier.append((SX,SY))
    Directions = [(0,1),(0,-1),(1,0),(-1,0)]
    VertSideList = []
    HoriSideList = []
    while ImperialFrontier:
        X, Y = ImperialFrontier.popleft()
        SkipSet.add((X,Y))
        if (X,Y) in ImperialCore:
            continue
        ImperialCore.add((X,Y))
        Perimeter += 4

        for DX, DY in Directions:
            NeWLoc = (X+DX,Y+DY) 
            if NeWLoc not in CoordDict[Letter]:
                if DX == 0:
                    Side = (Y+(DY/2), X, DY)
                    HoriSideList.append(Side)
                else:
                    Side = (X+(DX/2), Y, DX)
                    VertSideList.append(Side)
            if NeWLoc in CoordDict[Letter] and NeWLoc not in ImperialCore:
                Perimeter -= 2
                ImperialFrontier.append(NeWLoc)
    
    
    VertSideList.sort()
    for v in reversed(range(len(VertSideList))):
        Cur, Next = VertSideList[v], VertSideList[v-1]
        CX, CY, CD = Cur
        NX, NY, ND = Next
        if NX == CX and NY == CY - 1 and CD == ND:
            del VertSideList[v]
    HoriSideList.sort()
    for v in reversed(range(len(HoriSideList))):
        Cur, Next = HoriSideList[v], HoriSideList[v-1]
        CY, CX, CD = Cur
        NY, NX, ND = Next
        if NY == CY and NX == CX - 1 and CD == ND:
            del HoriSideList[v]
    

    Area = len(ImperialCore)
    Sides = len(VertSideList)+len(HoriSideList)
    return Area*Perimeter, Area*Sides

Part1Answer = 0
Part2Answer = 0
for y, f in enumerate(InputList):
    for x, c in enumerate(f):
        if (x,y) in SkipSet:
            continue
        NewLetter = CoordDict[(x,y)]
        P1, P2 = Region(x,y,NewLetter)
        Part1Answer += P1
        Part2Answer += P2

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
