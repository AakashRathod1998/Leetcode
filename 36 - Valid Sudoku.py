class Solution(object):
    def isValidSudoku(self, board):

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True

        # res = []
        # for i in range(9):
        #     for j in range(9):
        #         element = board[i][j]
        #         if element != '.':
        #             res += [(i, element), (element, j), (i // 3, j // 3, element)]
        # print(res)
        # return len(res) == len(set(res))
