import pdb
class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':

        # iterate through graph, each time you hit land
            # run breath first search
            # if node is land, convert '1' to 'X' and add neighbors to queue
            # if node is water, do nothing
            # when breath first search is complete, add 1 to island counter

            islands = 0
            if grid and grid[0]:

                row, col = len(grid), len(grid[0])
                for i in range(row):
                    for j in range(col):

                        if grid[i][j] == "1":
                            self.BFS_islands(grid, i, j)
                            islands += 1

            return islands


    def is_valid_neighbor(self, grid, i, j):
        return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == "1"

    def BFS_islands(self, grid, i, j):

        q = []
        q.append((i,j))
        grid[i][j] = 'X'

        # if queue is empty
        while q:

            i, j = q.pop(0)



            # if i == 6 and j == 6:
            #     pdb.set_trace()

            # add neighbors
            if self.is_valid_neighbor(grid, i-1, j):
                q.append((i-1, j))
                grid[i-1][j] = 'X'
            if self.is_valid_neighbor(grid, i, j-1):
                q.append((i, j-1))
                grid[i][j-1] = 'X'
            if self.is_valid_neighbor(grid, i, j+1):
                q.append((i, j+1))
                grid[i][j+1] = 'X'
            if self.is_valid_neighbor(grid, i+1, j):
                q.append((i+1, j))
                grid[i+1][j] = 'X'

            print(q)



x = Solution()
print(x.numIslands([["1","1","1","1","1","1","1"],["0","0","0","0","0","0","1"],["1","1","1","1","1","0","1"],["1","0","0","0","1","0","1"],["1","0","1","0","1","0","1"],["1","0","1","1","1","0","1"],["1","1","1","1","1","1","1"]]))
