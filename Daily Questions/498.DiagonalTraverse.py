class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        row = len(mat)
        col = len(mat[0])
        ans = []
        i = 0
        j = 0

        while len(ans) < row * col:
            ans.append(mat[i][j])
            if up:
                # 往右上走
                if j == col - 1:
                    # 到达最右边
                    i += 1
                    up = False
                elif i == 0:
                    # 到达最上边
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1

            else:
                # 往左下走
                if i == row - 1:
                    # 到达最左边
                    j += 1
                    up = True
                elif j == 0:
                    # 到达最下边
                    i += 1
                    up = True
                else:
                    i += 1
                    j -= 1

        return ans
