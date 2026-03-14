import random

def generate_maze(width,height):

    maze = [[1]*width for i in range(height)]

    x = 1
    y = 1

    stack = [(x,y)]

    maze[y][x] = 0

    while stack:

        x,y = stack[-1]

        directions = []

        if x>2 and maze[y][x-2]==1:
            directions.append((-2,0))

        if x<width-3 and maze[y][x+2]==1:
            directions.append((2,0))

        if y>2 and maze[y-2][x]==1:
            directions.append((0,-2))

        if y<height-3 and maze[y+2][x]==1:
            directions.append((0,2))

        if directions:

            dx,dy = random.choice(directions)

            maze[y+dy][x+dx] = 0
            maze[y+dy//2][x+dx//2] = 0

            stack.append((x+dx,y+dy))

        else:
            stack.pop()

    return maze
