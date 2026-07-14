class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)     
        cols = collections.defaultdict(set)     
        squares = collections.defaultdict(set)  

        # Iterate over every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":          # skip empty cell
                    continue

                # Determine which 3x3 sub-box this cell belongs to
                box_key = (r // 3, c // 3)

                # Check if current digit already exists in its row, column or sub-box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[box_key]):
                    return False        # duplicate found so mean is invalid Sudoku

                # Add the digit to the corresponding sets
                rows[r].add(val)
                cols[c].add(val)
                squares[box_key].add(val)

        # No duplicates found mean it is valid
        return True
