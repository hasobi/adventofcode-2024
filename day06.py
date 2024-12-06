## P1
carte = [ ]
dir = 0+1j

# Edit input file below
with open('day6.txt','r') as f:
    for ligne in f.read().splitlines():
        carte.append(ligne)

carte.reverse()
amax = len(carte[0])
bmax = len(carte)

for a,ligne in enumerate(carte):
    for b in range(len(carte[a])):
        if carte[b][a] == '^':
            start = complex(a,b)
            break

def get(carte, pos, dir):
    npos = pos + dir
    return carte[int(npos.imag)][int(npos.real)]

def isvalid(pos):
    a, b = int(pos.real), int(pos.imag)
    return 0 <= b < bmax and 0 <= a < amax


pos = start
visited = set([start])
while isvalid(pos+dir):
    if get(carte,pos,dir) in '.^':
        pos = pos + dir
        visited.add(pos)
    elif get(carte,pos,dir) == '#':
        dir = dir*(-1j)

print('Part 1 :', len(visited))

oldvisited = visited.copy()

## P2
def get(carte, pos, dir, obs):
    npos = pos + dir
    if npos == obs:
        return '#'
    else:
        return carte[int(npos.imag)][int(npos.real)]

obstructions = set()

possibleobs = [ (int(p.real), int(p.imag)) for p in oldvisited]
for (x,y) in possibleobs:
    pos = start
    dir = 0+1j
    obs = complex(x,y)
    states = set([(start, dir)])
    visited = set([start])
    while (pos+dir, dir) not in states and isvalid(pos+dir):
        if get(carte,pos,dir,obs) in '.^':
            pos = pos + dir
            visited.add(pos)
            states.add((pos,dir))
        elif get(carte,pos,dir,obs) == '#':
            dir = dir*(-1j)
    if (pos+dir, dir) in states:
        obstructions.add(obs)
print('Part 2 :', len(obstructions))