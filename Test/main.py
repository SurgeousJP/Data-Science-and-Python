# create a queue using deque
        q = deque()
        # save row and col for convenience
        rows = len(grid)
        cols = len(grid[0])
        # update variables : times, fresh
        minutes, freshs = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshs += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        # directions:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q and freshs:
            for i in range(len(q)):
                rRow, cCol = q.popleft()
                for r, c in directions:
                    rRow, cCol = rRow + r, cCol + c
                    if rRow < 0 or rRow == rows or cCol < 0 or cCol == cols or grid[rRow][cCol] != 1:
                        continue
                    grid[rRow][cCol] = 2
                    q.append([rRow, cCol])
                    freshs -= 1
            minutes += 1
        return minutes if freshs == 0 else -1