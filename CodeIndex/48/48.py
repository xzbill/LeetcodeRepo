class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        n=4:0,0->0,3;1,0->0,2;3,0->0,0;0,1->1,3;2,2->2,1;3,2->2,0;
        n:[i,j]->[j,n+1-i];[j,n+1-i]->[n+1-i,n+1-j];[n+1-i,n+1-j]->[n+1-j,i];[n+1-j,         i]->[i,j]
        n=3:0,0->0,2;0,1->1,2
        """
        n=len(matrix)
        if n % 2 == 0:
            for i in range((n)//2):
                for j in range((n)//2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n-1-j][i]
                    matrix[n - 1 - j][i] = matrix[n-1-i][n-1-j]
                    matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                    matrix[j][n - 1 - i] = temp

                    # 逆时针
                    # matrix[i][j] = matrix[j][n-1-i]
                    # matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
                    # matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                    # matrix[n-1-j][i] = temp
        else:
            for i in range((n-1)//2):
                for j in range((n+1)//2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n - 1 - j][i]
                    matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                    matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                    matrix[j][n - 1 - i] = temp
                    # matrix[i][j] = matrix[j][n-1-i]
                    # matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
                    # matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                    # matrix[n-1-j][i] = temp


# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
matrix = [
  [ 5, 1, 9, 11],
  [ 2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
]
s=Solution()
s.rotate(matrix)
print(1)
