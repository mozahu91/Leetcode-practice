class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i + 1, j)
                return 1
            return 0

        count = sum(dfs(i, j) for i in range(n) for j in range(m))
        return count

t = Solution()
grid = [['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']]
print(t.numIslands(grid))
