​
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memoization: dict(Tuple[int, int]) = {}
        to_rtrn = []
        for j in range(0, rowIndex+1):
             to_rtrn.append(self.helper(rowIndex, j, memoization))
        return to_rtrn
        
    def helper(self, i: int, j: int, memoization) -> int:
        
        if j == 0 or j == i: return 1
        else:
            # return self.helper(i-1, j - 1, memoization) + self.helper(i - 1, j, memoization) 
            if (i, j) in memoization:
                return memoization[(i,j)]
            else:
                val = self.helper(i-1, j - 1, memoization) + self.helper(i - 1, j, memoization) 
                memoization[(i,j)] = val
                return val
