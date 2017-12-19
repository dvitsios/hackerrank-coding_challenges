import sys

def getConnectedCells(i, j, n, m):
    
    con_cells = []
    
    if i >= 1:
        if j >= 1:
            con_cells.append([i-1, j-1])
        con_cells.append([i-1, j])
        if j < m-1:
            con_cells.append([i-1, j+1])
    
    if i < n-1:
        if j >= 1:
            con_cells.append([i+1, j-1])
        con_cells.append([i+1, j])
        if j < m-1:
            con_cells.append([i+1, j+1])
    
    if j >= 1:
        con_cells.append([i, j-1])
    if j < m-1:
        con_cells.append([i, j+1])
    
    return con_cells

    
def getRegion(i, j, visited, grid, l=1):
    n, m = len(grid), len(grid[0])
    con_cells = getConnectedCells(i, j, n, m)
    
    for cell in con_cells:
        
        if str(cell[0])+'_'+str(cell[1]) in visited:
            continue
        else:
            visited[str(cell[0])+'_'+str(cell[1])] = 1
            if grid[cell[0]][cell[1]] == 1:
                #print('l += 1')
                l += 1
                l = getRegion(cell[0], cell[1], visited, grid, l)
            
    return l
        
    
def getBiggestRegion(grid, visited = {}):
    n,m = len(grid), len(grid[0])
    
    all_region_sizes = []
    
    for i in range(n):
        for j in range(m):
            if str(i)+'_'+str(j) in visited:
                continue
            else:
                visited[str(i)+'_'+str(j)] = 1
                if grid[i][j] == 1:
                    #print('Calling getRegion...')
                    new_region_len = getRegion(i, j, visited, grid)
                    #print(new_region_len)
                    #print('visited:', visited)
                    all_region_sizes.append(new_region_len)
    
    return max(all_region_sizes)

    
n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))