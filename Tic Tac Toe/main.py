import math
import random


class Player:
    def __init__(self, letter):
        # define the player is 'x' or 'o'
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        val = None
        while not valid_move:
            val = int(input(self.letter + '\'s turn.' 'Input move (0, 9): '))
            try:
                if val not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalid move. Please try again')

        return val



class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # keeps track the board
        self.current_winner = None  # Keeps track whether the game has winner or not

    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        # tell us what number correspond to what box
        number_board = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for i, spot in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)

    def empty_square(self):
        return ' ' in self.board

    def empty_square_nums(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """0    1   2
           3    4   5
           6    7   8"""
        # check rows
        row_idx = square // 3
        row = self.board[row_idx*3:(row_idx+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check cols
        col_idx = square % 3
        col = [self.board[col_idx + i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonals but only for square that has even num
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, o_player, x_player, print_game=True):
    # return the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()

    # choose 'X' as starting letter
    letter = 'X'

    # iterate while the board still has empty spaces, the loop ends when there is a winner
    while game.empty_square():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")  # indicates the move made
                game.print_board()  # print the game board
                print('')  # empty line

            # Check whether the game has the winner or not
            if game.current_winner:
                if print_game:
                    print(letter + ' wins !')
                return letter

            # After making a move, we need to alternate the letters
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie !')


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, o_player, x_player, print_game=True)
