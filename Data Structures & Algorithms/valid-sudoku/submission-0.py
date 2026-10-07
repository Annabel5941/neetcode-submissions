from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [1,2,3,4,5,6,7,8,9]

        for i in range(9):
            #row counter
            row = board[i]
            rowCounter = Counter(row)

            #column counter
            col = [board[n][i] for n in range(9)]

            colCounter = Counter(col)

            #check each value
            for n in nums:
                if colCounter[str(n)] > 1 or rowCounter[str(n)] > 1:
                    return False

        #boxes
        for i in range(3):
            for j in range(3):
                box = []
                for k in range(3):
                    for l in range(3):
                        box.append(board[3*i+k][3*j+l])

                boxCounter = Counter(box)

                #check each value
                for n in nums:
                    if boxCounter[str(n)] > 1:
                        return False

        return True



        