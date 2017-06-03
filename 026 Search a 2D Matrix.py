"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true

i -> [i // n][i % n] Uses Binary Search Method
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = m*n-1
        
        while l<=h:
            mid = l+(h-l)//2
            if matrix[mid //2][mid %n]==target:
                return True
            elif matrix[mid //2][mid % n] < target:
                l = mid-1
            else:
                h = mid+1
        return False
