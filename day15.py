with open('day15.txt', 'r') as file:
    room, move = file.read().split('\n\n')
 
move = move.replace('\n', '')
walls = []
boxes = []
wide_boxes = []
 
for line in room.splitlines():
    cur_walls = []
    cur_boxes = []
 
    cur_wide_boxes = []
    for char in line:
        if char == '#':
            cur_walls.append(True)
            cur_boxes.append(False)
 
            cur_wide_boxes += [None, None]
        elif char == 'O':
            cur_walls.append(False)
            cur_boxes.append(True)
 
            cur_wide_boxes += [1, -1]
        else:
            if char == '@':
                x = x2 = len(walls)
                y = len(cur_walls)
                y2 = len(cur_wide_boxes)
            cur_walls.append(False)
            cur_boxes.append(False)
 
            cur_wide_boxes += [None, None]
    walls.append(cur_walls)
    boxes.append(cur_boxes)
    wide_boxes.append(cur_wide_boxes)
 
directions = {
    '^' : (-1, 0),
    '>' : ( 0, 1),
    'v' : ( 1, 0),
    '<' : ( 0,-1)
    }
 
# Part 1
 
for char in move:
    dx, dy = directions[char]
    i = 1
    while boxes[x + i*dx][y + i*dy]:
        i += 1
    if not walls[x + i*dx][y + i*dy]:
        boxes[x + i*dx][y + i*dy] = boxes[x + dx][y + dy]
        boxes[x + dx][y + dy] = False
        x += dx
        y += dy
 
gps = 0
for i, row in enumerate(boxes):
    for j, box in enumerate(row):
        if box:
            gps += 100*i + j
print(gps)
 
# Part 2
 
x, y = x2, y2
 
def canMove(x,y,dx):
    dy = wide_boxes[x][y]
    if dy:
        return canMove(x+dx,y,dx) and canMove(x+dx,y+dy,dx)
    return not walls[x][y//2]
 
def moveBoxes(x,y,dx):
    dy = wide_boxes[x][y]
    if dy:
        moveBoxes(x+dx,y,dx)
        moveBoxes(x+dx,y+dy,dx)
        wide_boxes[x+dx][y] = wide_boxes[x][y]
        wide_boxes[x+dx][y+dy] = wide_boxes[x][y+dy]
        wide_boxes[x][y] = None
        wide_boxes[x][y+dy] = None
        
 
for char in move:
    dx, dy = directions[char]
    if dx:
        if canMove(x+dx,y,dx):
            moveBoxes(x+dx,y,dx)
            x += dx
    else:
        i = 1
        while wide_boxes[x][y+i*dy]:
            i += 1
        if not walls[x][(y+i*dy)//2]:
            wide_boxes[x].insert(y, wide_boxes[x].pop(y+i*dy))
            y += dy
 
gps = 0
for i, row in enumerate(wide_boxes):
    for j, box in enumerate(row):
        if box == 1:
            gps += 100*i + j
print(gps)
