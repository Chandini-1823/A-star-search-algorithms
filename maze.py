class Maze:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def passable(self, pos):
        r, c = pos
        return self.grid[r][c] == 0

    def neighbors(self, pos):
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        result = []
        for dr, dc in dirs:
            next_pos = (pos[0]+dr, pos[1]+dc)
            if self.in_bounds(next_pos) and self.passable(next_pos):
                result.append(next_pos)
        return result

    def visualize(self, path=None, visited=None):
        for r in range(self.rows):
            row = ""
            for c in range(self.cols):
                if (r, c) == self.start:
                    row += "S "
                elif (r, c) == self.goal:
                    row += "G "
                elif path and (r, c) in path:
                    row += "* "
                elif visited and (r, c) in visited:
                    row += ". "
                elif self.grid[r][c] == 1:
                    row += "$ "
                else:
                    row += "  "
            print(row)
