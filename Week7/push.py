import util
	

def push_up(grid):     
	    old_grid = util.copy_grid(grid)
	    while len(grid) > 0:
	        del grid[0]
	    util.create_grid(grid)      
	    for col in range(4):
	        pos = 0
	        merge = 0
	        for row in range(4):
	            if old_grid[row][col] == grid[merge][col]:
	                grid[merge][col] += old_grid[row][col]
	                merge += 1
	            else:
	                grid[pos][col] = old_grid[row][col]
	                pos += 1
	                if pos-merge >= 2:
	                    merge += 1
	

def push_down(grid):  
	    old_grid = util.copy_grid(grid)  
	    while len(grid) > 0:
	            del grid[0]
	    util.create_grid(grid)   
	    for col in range(4):
	        pos = 3
	        merge = 3
	        for row in range(3,-1,-1):
	            if old_grid[row][col] != 0:
	                if old_grid[row][col] == grid[merge][col]:
	                    grid[merge][col] += old_grid[row][col]
	                merge -= 1
	            else:
	                grid[pos][col] = old_grid[row][col]
	                pos -= 1
	                if merge - pos >= 2:
	                    merge -= 1    
	

def push_right(grid):   
	    old_grid = util.copy_grid(grid) 
	    while len(grid) > 0:
	        del grid[0]
	    util.create_grid(grid)      
	    for row in range(4): 
	        pos = 3
	        merge = 3
	        for col in range(3,-1,-1):
	            if old_grid[row][col] != 0:
	                if old_grid[row][col] == grid[row][merge]:
	                    grid[row][merge] += old_grid[row][col]
	                    merge -= 1
	                else:
	                    grid[row][pos] = old_grid[row][col]
	                    pos -= 1
	                    if merge - pos >= 2:
	                        merge -= 1         
	

def push_left(grid):  
	    old_grid = util.copy_grid(grid) 
	    while len(grid) > 0:
	        del grid[0]
	    util.create_grid(grid)   
	    for row in range(4): 
	        pos = 0
	        merge = 0
	        for col in range(4):
	            if old_grid[row][col] != 0:
	                if old_grid[row][col] == grid[row][merge]:
	                    grid[row][merge] += old_grid[row][col]
	                    merge += 1
	                else:
	                    grid[row][pos] = old_grid[row][col]
	                    pos += 1
	                    if pos - merge >= 2:
	                        merge += 1  
