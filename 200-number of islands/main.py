class Solution:
    def numIslands(self, grid):
        self.islands_num = 0
        self.grid = grid
        self.row = len(grid)

        if self.row == 0:
            return 0

        self.column = len(grid[0])
        if self.column == 0:
            return 0

        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j] == "1":
                    self.islands_num += 1
                    self.dspIslands(i, j)
        return self.islands_num

    def dspIslands(self, i, j):
        if i < 0 or j < 0 or i >= self.row or j >= self.column or self.grid[i][j] == "0":
            return
        else:
            self.grid[i][j] = "0"
            self.dspIslands(i+1, j)
            self.dspIslands(i-1, j)
            self.dspIslands(i, j-1)
            self.dspIslands(i, j+1)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

grid3 = []

grid4 = ["1", "1"]

solution = Solution()
print(solution.numIslands(grid3))