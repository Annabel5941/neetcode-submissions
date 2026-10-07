class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #just binary search each row?
        for row in matrix:

            low = 0
            high = len(row)-1

            while high >= low:
                mid = (low+high)//2
                val = row[mid]

                if val == target:
                    return True

                elif val < target:
                    low = mid+1

                else:
                    high = mid-1
        
        return False