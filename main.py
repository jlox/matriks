from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix(4, 4)

for angle in range(90):
    x = int(XRES * math.cos(math.radians(angle)))
    y = int(YRES * math.sin(math.radians(angle)))
    x0 = x
    y0 = YRES - y
    x1 = XRES - x
    y1 = y
    add_edge(edges, x0, y0, 0, x1, y1, 0)
    rotate = make_rotX(1)
    edges = matrix_mult(rotate, edges)
draw_lines(edges, screen, color)

display(screen)
