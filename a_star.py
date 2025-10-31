import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star_search(maze):
    start, goal = maze.start, maze.goal
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()
    
    while frontier:
        _, current = heapq.heappop(frontier)
        visited.add(current)
        if current == goal:
            return reconstruct_path(came_from, start, goal), visited

        for next_pos in maze.neighbors(current):
            new_cost = cost_so_far[current] + 1 # All steps cost 1
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost + heuristic(next_pos, goal)
                heapq.heappush(frontier, (priority, next_pos))
                came_from[next_pos] = current
    return None, visited

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            return None  # No path
    path.append(start)
    path.reverse()
    return path
