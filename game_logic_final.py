import numpy, random
def make_grid(grid,grid_size_v,grid_size_h,mines):
    mine_count = 0
    #grid = numpy.zeros((grid_size_h,grid_size_v))
    temp_mines = mines
    while temp_mines:
        mine_row = random.randrange(0,grid_size_v)
        mine_column = random.randrange(0,grid_size_h)
        if grid[mine_row][mine_column] != -1:
            grid[mine_row][mine_column] = -1
            temp_mines-=1
            if mine_column+1<grid_size_h and grid[mine_row][mine_column+1]!=-1:
                grid[mine_row][mine_column+1]+=1
            if mine_row+1<grid_size_v and mine_column+1<grid_size_h and grid[mine_row+1][mine_column+1]!=-1:
                grid[mine_row+1][mine_column+1]+=1
            if mine_column-1>=0 and grid[mine_row][mine_column-1]!=-1:
                grid[mine_row][mine_column-1]+=1
            if mine_row+1<grid_size_v and grid[mine_row+1][mine_column]!=-1:
                grid[mine_row+1][mine_column]+=1
            if mine_row-1>=0 and grid[mine_row-1][mine_column]!=-1:
                grid[mine_row-1][mine_column]+=1
            if mine_row+1<grid_size_v and mine_column-1>=0 and grid[mine_row+1][mine_column-1]!=-1:
                grid[mine_row+1][mine_column-1]+=1
            if mine_row-1>=0 and mine_column+1<grid_size_h and grid[mine_row-1][mine_column+1]!=-1:
                grid[mine_row-1][mine_column+1]+=1
            if mine_row-1>=0 and mine_column-1>=0 and grid[mine_row-1][mine_column-1]!=-1:
                grid[mine_row-1][mine_column-1]+=1
    return grid
#make_grid()
#give_value(2,2)