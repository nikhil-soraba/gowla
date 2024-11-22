from collections import deque

def dfs(grid, pos, visited):
    M, N = len(grid), len(grid[0])
    row, col = pos

    if (row < 0) or (col < 0) or \
       (row >= M) or (col >= N) or \
       (pos in visited):
        return

    visited.add(pos)

    dfs(grid, (row + 1, col), visited)
    dfs(grid, (row - 1, col), visited)
    dfs(grid, (row, col + 1), visited)
    dfs(grid, (row, col - 1), visited)

dirs = [ (0,1), (0,-1), (1,0), (-1,0) ]

def bfs(grid, pos):
    M, N = len(grid), len(grid[0])

    fifo = deque([pos])
    visited = set([pos])

    while fifo:
        pos = fifo.popleft()
        row, col = pos

        for r_off, c_off in dirs:
            n_row = row + r_off
            n_col = col + c_off
            n_pos = (n_row, n_col)
            
            if (n_row < 0) or (n_col < 0) or \
               (n_row >= M) or (n_col >= N) or \
               (n_pos in visited):
                continue
            
            visited.add(n_pos)
            fifo.append(n_pos)
