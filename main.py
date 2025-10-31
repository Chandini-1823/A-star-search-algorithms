from maze import Maze
from a_star import a_star_search, reconstruct_path

def main():
    # Example Maze (0 = free, 1 = wall)
    # S = Start, G = Goal
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (1, 1)
    goal = (3, 3)

    maze = Maze(grid, start, goal)
    path, visited = a_star_search(maze)
    if path:
        print("Shortest path found:")
        print(path)
    else:
        print("No path found.")

    # Optional: Visualize
    maze.visualize(path, visited)

if __name__ == "__main__":
    main()
