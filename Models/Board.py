
class Board:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.board = [[None for _ in range(boardsize)] for _ in range(boardsize)]

    def add_piece(self, row, col, playing_piece):
        if self.board[row][col] is not None:
            return False
        self.board[row][col] = playing_piece
        return True

    def get_free_cells(self):
        freecells = []
        for i in range(self.boardsize):
            for j in range(self.boardsize):
                if self.board[i][j] is None:
                    freecells.append((i,j))
        return freecells

    def print_board(self):
        for i in range(self.boardsize):
            rowrepresent = []
            for j in range(self.boardsize):
                if self.board[i][j] is not None:
                    rowrepresent.append(f"{self.board[i][j].value}")
                else:
                    rowrepresent.append(" ")

            print(" | ".join(rowrepresent))
            print("-" * (self.boardsize * 4 - 1))  # separator line