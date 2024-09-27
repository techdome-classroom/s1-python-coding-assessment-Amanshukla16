class Solution:
   
   def count_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 'L':
            grid[i][j] = 'V'
            dfs(i + 1, j)  
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L':
                count += 1
                dfs(i, j)
                return count
                
    grid = [
    ["L", "L", "W", "W", "W"],
    ["L", "W", "W", "W", "W"],
    ["W", "W", "L", "L", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "W", "L"],
    ]
  
    print(count_islands(grid))
    return 0
