

class TicTacToe:
    def __init__(self):
        """Start a new game"""
        self._board = [[' '] * 3 for i in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """Put an X or O mark at the position (i, j) for next player's turn """
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self._board[i][j] != ' ':
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game has already completed")
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        board = self._board  # local variable for shorthand !!!
        return (board[0][0] == board[0][1] == board[0][2] != ' ' or
                board[1][0] == board[1][1] == board[1][2] != ' ' or
                board[2][0] == board[2][1] == board[2][2] != ' ' or
                board[0][0] == board[1][0] == board[2][0] != ' ' or
                board[0][1] == board[1][1] == board[2][1] != ' ' or
                board[0][2] == board[1][2] == board[2][2] != ' ' or
                board[0][0] == board[1][1] == board[2][2] != ' ' or
                board[2][0] == board[1][1] == board[0][2] != ' ' )

    def winner(self):
        """Return mark indicating the winner, if None then call it a Tie"""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        """return string representation of the game board"""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)


if __name__ == '__main__':
    game = TicTacToe()
    # X moves: # O moves:

    game.mark(1, 1)
    game.mark(0, 2)
    game.mark(2, 2)
    game.mark(0, 0)
    game.mark(0, 1)
    game.mark(2, 1)
    game.mark(1, 2)
    game.mark(1, 0)
    game.mark(2, 0)
    print(str(game))
    winner = game.winner()
    if winner is None:
        print("Tie !!!")
    else:
        print(winner, "wins")