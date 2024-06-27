import drawsvg as dsvg

def draw_binary_tree(x, y, level, max_level, d):
    if level > max_level:
        return
    
    X_OFFSET = 0 # Adjusted to move the tree towards the center
    Y_OFFSET = 100 # Adjusted to move the tree towards the center

    # Calculate positions for left and right children
    leaf_spacing = 20  # Spacing between leaves
    offset = leaf_spacing * (2 ** (max_level - level - 1))  # Calculate offset based on leaf spacing and level
    left_x, left_y = x - offset, y + 80  # Increase y-offset to make the tree taller
    right_x, right_y = x + offset, y + 80  # Increase y-offset to make the tree taller
    
    # Draw lines to children
    if level < max_level:
        d.append(
            dsvg.Line(
                x + X_OFFSET, y + Y_OFFSET, 
                left_x + X_OFFSET, left_y + Y_OFFSET, 
                stroke='black', stroke_width=6
            )
        )  # Increase stroke width and center on the screen
        
        d.append(
            dsvg.Line(
                x + X_OFFSET, y + Y_OFFSET, 
                right_x + X_OFFSET, right_y + Y_OFFSET, 
                stroke='black', stroke_width=6
            )
        )  # Increase stroke width and center on the screen
    
    # Draw the current node
    d.append(dsvg.Circle(x + X_OFFSET, y + Y_OFFSET, 12, fill='white'))  # Draw a white circle of slightly larger size first
    d.append(dsvg.Circle(x + X_OFFSET, y + Y_OFFSET, 10, fill='orange'))  # Then draw the original orange circle
    
    # Recursively draw the left and right subtrees
    draw_binary_tree(left_x, left_y, level + 1, max_level, d)
    draw_binary_tree(right_x, right_y, level + 1, max_level, d)

# Create a drawing object
d = dsvg.Drawing(width=1000, height=1000, origin='center')  # Adjusted the width and height to prevent cropping and accommodate the larger tree

# Draw the binary tree
draw_binary_tree(0, 0, 0, 4, d)  # Start drawing from level 0

# Save the drawing to an SVG file
d.save_svg('binary_tree.svg')
