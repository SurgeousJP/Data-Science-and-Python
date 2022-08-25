def solveNQueens(self, n: int):
        cols = set()
        negDiag = set()
        posDiag = set()
        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or r - c in negDiag or r + c in posDiag:
                    continue

                cols.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = '.'

            return res