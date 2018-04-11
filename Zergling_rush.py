import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



w, h = [int(i) for i in input().split()]
check = [[0 for x in range(w)] for y in range(h)] 
where = ['top','left', 'right', 'bottom']
#print(check)
row = []
for i in range(h):
    row.append(list(input()))


def move(position):
    check[position[0]][position[1]] = 1
    # move LEFT
    if position[0] != 0:
        if row[position[0]-1][position[1]] =='.' and check[position[0]-1][position[1]] == 0:
            move([position[0]-1,position[1]])
    # move RIGHT
    if position[0] != h-1:
        if row[position[0]+1][position[1]] =='.' and check[position[0]+1][position[1]] == 0:
            move([position[0]+1,position[1]])
    # move TOP
    if position[1] != 0:
        if row[position[0]][position[1]-1] =='.' and check[position[0]][position[1]-1] == 0:
            move([position[0],position[1]-1])
    # move DOWN
    if position[1] != w-1:
        if row[position[0]][position[1]+1] =='.' and check[position[0]][position[1]+1] == 0:
            move([position[0],position[1]+1])


for wh in where:
    #from TOP and BOTTOM
        for i in range(w):
            if row[0][i] =='.':
                move([0,i])
            if row[h-1][i] =='.':
                move([h-1, i])
    
    #from LEFT and RIGHT
        for j in range(h):
            if row[j][0] =='.':
                move([j, 0])
            if row[j][w-1] =='.':
                move([j, w-1])
            
for i,line in enumerate(row):
    for j,base in enumerate(line):
        if base == 'B':
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if check[x][y] == 1:
                        row[x][y] = 'z'


for a in row:
    for b in a:
        print(b, end="")
    print()
#print(row)
