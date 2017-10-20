import turtle

class Maze:
    def __init__(self):
        self.maze_list = []
    def load_maze(self, str_data):
        '''
        str_data is an array of string presenting maze
        '''
        for row in str_data:
            maze_row = []
            for c in row:
                maze_row.append(c)
            self.maze_list.append(maze_row)

    def draw_maze(self, turtle_instance):
        '''
        to visualize maze with turtle
        '''
        for row in range(len(self.maze_list)):
            self.draw_row(row, turtle_instance)
    def resolve_maze(self, start_row, start_col, turtle_instance):
        '''
        to resolve maze start from start_row, start_col, using turtle for visualization

        if self.maze_list[x][y] is on border and not wall, maze is resolved
        '''
        #initialize data
        for row in self.maze_list:
            for block in row:
                if block != "+":
                    block = " "
        #self.resolve_maze_internal(start_row, start_col, turtle_instance)
        self.dfs(start_row, start_col, turtle_instance)

    def get_neighbors(self, row, col, visited):
        rows = len(self.maze_list)
        cols = len(self.maze_list[0])
        row_test = row -1
        col_test = col
        neighbors = []
        if row_test >= 0 and self.maze_list[row_test][col] != '+' and (row_test, col_test)  not in visited:
            neighbors.append( (row_test, col_test))
        row_test = row + 1
        col_test = col
        if row_test < rows and self.maze_list[row_test][col_test] != '+' and (row_test, col_test)  not in visited:
            neighbors.append( (row_test, col_test))
        col_test = col -1
        row_test = row
        if col_test >= 0 and self.maze_list[row_test][col_test] != '+' and (row_test, col_test)  not in visited:
            neighbors.append( (row_test, col_test ) )
        col_test = col + 1
        row_test = row
        if col_test < cols and self.maze_list[row_test][col_test] != '+' and (row_test, col_test)  not in visited:
            neighbors.append( ( row_test, col_test) )
        return neighbors
        
    def dfs(self, start_row, start_col, turtle_instance):
        stack = [(start_row, start_row)]
        visited = set()
        while stack:
            row, col = stack.pop()
            self.maze_list[row][col] = '<'
            self.draw_block_with_index(row, col, turtle_instance)
            if (row == 0 or row == len(self.maze_list) - 1) and self.maze_list[row][col] != '+':
               return True#maze get resolved
            if (col == 0 or col == len(self.maze_list[0]) - 1) and self.maze_list[row][col] != '+':
               return True
            visited.add((row, col))

            #get neighbors
            for n in self.get_neighbors(row, col, visited ):
                stack.append(n)

    def resolve_maze_internal(self, row, col, turtle_instance):
        '''
        internal help to resolve maze
        '''
        if row < 0 or row >= len(self.maze_list):
            return False
        if col < 0  or col >= len(self.maze_list[0]):
            return False
        if (row == 0 or row == len(self.maze_list) - 1) and self.maze_list[row][col] != '+':
            return True#maze get resolved
        if (col == 0 or col == len(self.maze_list[0]) - 1) and self.maze_list[row][col] != '+':
            return True

        if self.maze_list[row][col] == ' ':
            self.maze_list[row][col] = '-'
        elif self.maze_list[row][col] == '+':
            return False
        elif self.maze_list[row][col] == '-':
            self.maze_list[row][col] = '<'#back path
            return False

        self.draw_block_with_index(row, col, turtle_instance)

        print("pos", row, col, self.maze_list[row][col])
        if (self.resolve_maze_internal(row, col+1, turtle_instance) or
           self.resolve_maze_internal(row, col-1, turtle_instance) or
           self.resolve_maze_internal(row-1, col, turtle_instance) or
           self.resolve_maze_internal(row+1, col, turtle_instance) ):
            return True

    def draw_block(self, points, block_type, turtle_instance):
        '''
        draw a block on screen with given color
        '''
        color_for_block = "brown"
        color_for_space = "yellow"
        color_for_path = "green"
        color_for_visited = "blue"
        color_for_block_border = "black"
        color = None
        color_for_border = None
        if block_type == "+":
            color = color_for_block
            color_for_border = color_for_block_border
        elif block_type == '-':
            color = color_for_path
            color_for_border = color_for_path
        elif block_type == '<':
            color = color_for_visited
            color_for_border = color_for_visited
        else:
            color = color_for_space
            color_for_border = color_for_space

        turtle_instance.goto(points[0][0], points[0][1])
        turtle_instance.fillcolor(color)
        turtle_instance.pencolor(color_for_border)
        turtle_instance.pendown()
        turtle_instance.begin_fill()
        turtle_instance.goto(points[1][0], points[1][1])
        turtle_instance.goto(points[2][0], points[2][1])
        turtle_instance.goto(points[3][0], points[3][1])
        turtle_instance.goto(points[0][0], points[0][1])
        turtle_instance.end_fill()
        turtle_instance.penup()
    def draw_block_with_index(self, row, col, turtle_instance):
        size_x = 10
        size_y = 10
        x_start = -100
        y_start = 0
        start_point = [-100, 0]

        start_point = [x_start + size_x * 2 * col, y_start + size_y*2*row]
        points = [
                [start_point[0] - size_x, start_point[1] - size_y],
                [start_point[0] + size_x, start_point[1] - size_y],
                [start_point[0] + size_x, start_point[1] + size_y],
                [start_point[0] - size_x, start_point[1] + size_y]
            ]
        self.draw_block(points, self.maze_list[row][col], turtle_instance)


    def draw_row(self, row, turtle_instance):
        '''
        draw a row
        '''
        for col in range(len(self.maze_list[row])):
            self.draw_block_with_index(row, col, turtle_instance)


def test():
    maze_data = [
        "++ +++++++++++++++++++",#0
        "+   +   ++ ++     +  +",#1
        "+ +   +       +++ + ++",#2
        "+ + +  ++  ++++   + ++",#3
        "+++ ++++++    +++ +  +",#4
        "+          ++  ++    +",#5
        "+++++ ++++++   +++++ +",#6
        "+     +   +++++++  + +",#7
        "+ +++++++        +   +",#8
        "+                + +++",#9
        "++++++++++++++++++++++"#10
        ]
    a_maze = Maze()
    a_maze.load_maze(maze_data)

    turtle_instance = turtle.Turtle()
    turtle_instance.speed(10)
    window = turtle.Screen()
    a_maze.draw_maze(turtle_instance)
    #row = 1
    #col = 1
    row = 7
    col = 7
    a_maze.resolve_maze(row, col, turtle_instance)

    window.exitonclick()

test()