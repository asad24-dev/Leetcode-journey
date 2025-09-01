def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        rotten = []
        numoranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                    numoranges += 1
                elif grid[i][j] == 1:
                    numoranges += 1
        fresh = numoranges - len(rotten)
        if not fresh:
            return 0
        queue = collections.deque(rotten)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                coords = queue.popleft()
                row = coords[0]
                col = coords[1]
                for incr, incc in directions:
                    newr = row + incr
                    newc = col + incc
                    if not ((0 <= newr < rows) and  (0 <= newc < cols)):
                        continue
                    else:
                        if grid[newr][newc] == 1:
                            grid[newr][newc] = 2
                            queue.append((newr, newc))
                            fresh -=1
            minutes+=1
        if fresh > 0:
            return -1
        return minutes - 1