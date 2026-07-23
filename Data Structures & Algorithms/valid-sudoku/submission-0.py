class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            seen_r = set()
            for c in range(len(board[0])):
                current  = board[r][c]

                if current == '.':
                    continue

                if current in seen_r:
                    return False
                
                seen_r.add(current)
        for c in range(len(board[0])):
            seen_c = set()
            for r in range(len(board)):
                current = board[r][c]

                if current == '.':
                    continue
                if current in seen_c:
                    return False
                seen_c.add(current)
        
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                seen_b = set()

                for r in range(startRow, startRow+3):
                    for c in range(startCol,startCol+3):
                        current = board[r][c]
                        if current == '.':
                            continue
                        if current in seen_b:
                            return False
                        seen_b.add(current)
        return True
                