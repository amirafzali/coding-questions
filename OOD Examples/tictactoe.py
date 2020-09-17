from enum import Enum

class TileType(Enum):
    EMPTY, X, O = 0,1,2

class Tile:
    def __init__(self):
        self._type = TileType.EMPTY

    @property
    def tile_type(self):
        return self._type
    
    @tile_type.setter
    def tile_type(self, new_type):
        self._type = new_type

    def __eq__(self,a,b):
        return a.tile_type == b.tile_type

class Board:
    def __init__(self):
        self.create_board()

    def create_board(self):
        self._board = [[Tile() for j in range(3)] for i in range(3)]

    def change_tile(self, i, j, tile_type):
        if 0 <= i < 3 and 0 <= j < 3 and self._board[i][j].tile_type == TileType.EMPTY:
            self._board[i][j].tile_type = tile_type
            return self.check_win(i,j)

        return False

    def check_win(self,i,j):
        board = self._board
        if board[i][0] == board[i][1] == board[i][2] or board[0][j] == board[1][j] == board[2][j]:
            return True

        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            return True

        return False

class Game:
    def __init__(self):
        self._current_player = TileType.X
        self._board = Board()

    def start_game_loop(self):
        done = False
        while not done:
            move = self.prompt_move()

