# -*- coding: utf-8 -*-
import sys
import time
grids = [['*', '*', '*', '*', '0'],
         ['*', '0', '0', '*', '0'],
         ['*', '0', '*', '*', '0'],
         ['0', '*', '*', '*', '0'],
         ['0', '0', '*', '*', '0'],
        ]
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid or not grid[0]:return 0
        m,n=len(grid),len(grid[0])
        print( "%dx%d " % (m,n))
        vis = [[False for j in range(n)]for i in range(m)]
        self.direction = [[1,0], [0, -1], [-1, 0], [0, 1]]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0' and not vis[i][j]:
                    vis[i][j]=True
                    self.dfs(i,j,grid,vis)
                    ans+=1
        return ans

    def dfs(self,x,y,grid,vis):
        for k in range(4):
            nx, ny = x+ self.direction[k][0] , y + self.direction[k][1]
            if nx<0 or ny<0 or nx >=len(grid) or ny>=len(grid[0]) \
                    or grid[nx][ny]=='*' or vis[nx][ny]: continue
            vis[nx][ny]=True
            self.dfs(nx,ny,grid,vis)

if __name__ == '__main__':
    start_time = time.time()
    for i in range(len(grids)):
        print(grids[i])
    print( Solution().numIslands(grids) )
    elapse_time = time.time() - start_time
    print("elapse time :  ", elapse_time)