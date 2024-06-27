import random
import numpy as np
import drawsvg as draw

LEAF_SPACING = 20
NODE_SIZE = 10
BACKGROUND_SIZE = 12
LINE_WIDTH = 6
X_OFFSET = 0
Y_OFFSET = 100
INACTIVE_COLOR = 'lightgray'
ACTIVE_COLOR = 'orange'
ACTIVE_LINE_COLOR = 'black'
BACKGROUND_COLOR = 'white'
INACTIVE_LINE_STYLE = '5,5'  # Dotted line style for drawsvg
ACTIVE_LINE_STYLE = 'solid'

def draw_node(drawing, x, y, color):
    drawing.append(draw.Circle(x + X_OFFSET, y + Y_OFFSET, BACKGROUND_SIZE, fill=BACKGROUND_COLOR))
    drawing.append(draw.Circle(x + X_OFFSET, y + Y_OFFSET, NODE_SIZE, fill=color))

def draw_line(drawing, x1, y1, x2, y2, color, style):
    drawing.insert(0, draw.Line(x1 + X_OFFSET, y1 + Y_OFFSET, x2 + X_OFFSET, y2 + Y_OFFSET, stroke=color, stroke_width=LINE_WIDTH, stroke_dasharray=style))

def compute_inactivity(max_level, sparsity):
    num_leaves = 2 ** max_level
    inactive_leaves = np.random.rand(num_leaves) < sparsity
    inactive_nodes = np.zeros(2 ** (max_level + 1) - 1, dtype=bool)
    inactive_nodes[-num_leaves:] = inactive_leaves
    for i in range(num_leaves - 2, -1, -1):
        inactive_nodes[i] = inactive_nodes[2 * i + 1] and inactive_nodes[2 * i + 2]
    return inactive_nodes

def draw_tree(drawing, level, x, y, parent_x, parent_y, node_index, inactive_nodes, max_level):
    if level > max_level:
        return

    is_inactive = inactive_nodes[node_index]

    node_color = INACTIVE_COLOR if is_inactive else ACTIVE_COLOR
    line_color = INACTIVE_COLOR if is_inactive else ACTIVE_LINE_COLOR
    line_style = INACTIVE_LINE_STYLE if is_inactive else ACTIVE_LINE_STYLE

    if level != 0:
        draw_line(drawing, x, y, parent_x, parent_y, line_color, line_style)

    draw_node(drawing, x, y, node_color)

    offset = LEAF_SPACING * (2 ** (max_level - level - 1))
    draw_tree(drawing, level + 1, x - offset, y + 80, x, y, 2 * node_index + 1, inactive_nodes, max_level)
    draw_tree(drawing, level + 1, x + offset, y + 80, x, y, 2 * node_index + 2, inactive_nodes, max_level)

drawing = draw.Drawing(width=1000, height=1000, origin='center')
max_level = 4
sparsity = 0.725
inactive_nodes = compute_inactivity(max_level, sparsity)
draw_tree(drawing, 0, 0, 0, 0, 0, 0, inactive_nodes, max_level)
drawing.save_svg('binary_inactive_tree.svg')
