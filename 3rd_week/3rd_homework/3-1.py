from collections import deque


def find_shortest_way(grid):
    rows = len(grid)
    cols = len(grid[0])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    deq = deque([(0, 0)])
    distance = [[0] * cols for _ in range(rows)]
    distance[0][0] = 1

    while deq:
       x, y = deq.popleft()
       if x == rows - 1 and y == cols - 1:
           return distance[x][y]
       for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and distance[nr][nc] == 0:
                distance[nr][nc] = distance[x][y] + 1
                deq.append((nr, nc))

    return -1


grid = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
print(find_shortest_way(grid))

grid2 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

print(find_shortest_way(grid2))