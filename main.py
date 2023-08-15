"""
Main module that contains all the class and functions.

Classes
-------
Token
Player
Move
Game

Constants
---------
HORIZONTAL
VERTICAL
BOARD_SIZE

"""

from enum import Enum

# constants
HORIZONTAL = 7
VERTICAL = 6
BOARD_SIZE = HORIZONTAL * VERTICAL


class Token(Enum):
    F = "_"
    W = "w"
    B = "b"


class Player(Enum):
    White = 0
    Black = 1


class Move:
    """Class move that depicts certain features.

    Attributes
    ----------
    pos_y : int
    pos_x : int
    player : Player

    """
    def __init__(self, pos_y, pos_x, player):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.player = player


class Game:
    """Class that contains game logic and game execution.

    Attributes
    ----------
    turn : Player(Enum)
    turn_count : int
                 Number of turns already made.
    game_over : bool
                Boolean value if the game is won, lost or not playable.
    board : list[list[]]
            Matrix where the game takes place.
    move_list: list
               List with al past moves that where played.
    """

    turn: "Player"
    turn_count: int
    game_over: bool
    board = [[]]
    move_list: []

    def __init__(self):
        self.board = [[Token.F for _ in range(HORIZONTAL)] for _ in range(VERTICAL)]
        self.turn = Player.Black
        self.turn_count = 0
        self.game_over = False

    def move(self, move: "Move"):
        # check if game is over
        if self.game_over:
            print("Game is already over")
            return
        # check who's move it is
        if move.player != self.turn:
            print("Wrong turn")
            return
        # check if position is free
        if self.board[move.pos_x][move.pos_y] != Token.F:
            print(f"Token position is not free, a {self.board[move.pos_y][move.pos_x]} token is blocking")
            return

        if move.pos_y >= VERTICAL or move.pos_x >= HORIZONTAL:
            print(f"Token position is out of bounds."
                  f" Position: y:{move.pos_y}, x:{move.pos_x}")
            return
        # check under the new token position
        if move.pos_y+1 < VERTICAL and move.pos_x+1 < HORIZONTAL:
            if self.board[move.pos_y+1][move.pos_x] == Token.F:
                print(f"Token cannot be placed on position x: {move.pos_x}, y: {move.pos_y},"
                      f" free position on x: {move.pos_x}, y: {move.pos_y+1}")
                return

        # set token
        self.board[move.pos_x][move.pos_y] = move.player

        # end of move
        self.turn_count += 1
        if self.turn == Player.Black:
            self.turn = Player.White
        else:
            self.turn = Player.Black
        self.check_game_over()

    def check_game_over(self):
        # win of black
        # win of white
        # move is not possible and no one won (stalemate)
        pass

    def check_game_over_player(self):
        # vertical
        # horizontal
        # diagonal
        pass

    def print_board(self):
        for x in range(VERTICAL):
            for y in range(HORIZONTAL):
                print(self.board[x][y].value, end=" ")
            print()
        print()


if __name__ == "__main__":
    game = Game()
    game.print_board()

    game.move(Move(0, 6, Player.Black))
    # game.move(Move(1, 0, Player.White))
    game.print_board()




