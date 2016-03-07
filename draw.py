from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    #use draw_line to connect points in matrix
    size = len(matrix)
    point = 0
    while (point < size):
        draw_line(screen, matrix[point][0], matrix[point][1], matrix[point+1][0], matrix[point+1][1], color)
        point = point + 1
    return matrix

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    line=0
    pa=4
    parts=[x, y, z, 0]
    while (line < 4):
        if((matrix[line][0]==0) and (matrix[line][1]==0) and (matrix[line][2]==0) and (matrix[line][3]==0)):
            for p in range(pa):
                matrix[line][p] = parts[p]
            line=4
        else:
            line=line + 1
    return matrix

mat = new_matrix(4, 4)
print(add_point(mat, 1, 2, 0))
print(add_point(mat, 2, 1, 0))
print(add_point(mat, 2, 3, 0))
print(add_point(mat, 3, 2, 0))

def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
    elif dy == 0:
            y = y + 1
            x = x0
            while x <= x1:
                plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx