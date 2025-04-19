from collections import deque

from Models.Players import Players
from Models.Board import Board
from Models.PieceX import PieceX
from Models.PieceO import PieceO

class TicTacToeGame:
    def __init__(self):
        self.players_list = deque()
        self.game_board = None

    def initialize_game(self, boardsize):
        player1 = Players('Player1', PieceO())
        player2 = Players('Player2', PieceX())

        self.players_list.append(player1)
        self.players_list.append(player2)

        self.game_board = Board(boardsize)

    def start_game(self):
        winner = False

        while not winner:
            player_turn = self.players_list.popleft()
            print('------> ', player_turn.user)

            self.game_board.print_board()
            free_spaces:list = self.game_board.get_free_cells()
            if not free_spaces:
                winner = True
                continue

            move = input(f"Player: {player_turn.user}, enter row and col: ")
            try:
                row, col = map(int, move.split(","))
            except ValueError:
                print("Invalid input. Please enter as row,column")
                self.players_list.appendleft(player_turn)
                continue
            
            if not self.game_board.add_piece(row, col, player_turn.playing_piece.piece_type):
                print("Incorrect position chosen, try again.")
                self.players_list.appendleft(player_turn)
                continue
                
            self.players_list.append(player_turn)

            if self.winnerAvailable(row ,col , player_turn.playing_piece.piece_type):
                self.game_board.print_board()
                print(f"Winner: {player_turn.user}")
                return player_turn.user
        
        return "TIE!"
    

    def winnerAvailable(self, row, col, piece_type):
        size = self.game_board.boardsize
        board = self.game_board.board

        # ROW check
        if all(
            board[row][i] is not None and board[row][i] == piece_type
            for i in range(size)
        ): return True

        # COL check
        if all(
            board[i][col] is not None and board[i][col] == piece_type
            for i in range(size)
        ): return True

        # Both diagonals check
                # ROW check
        if row+col == size-1 and all(
            board[i][size-1-1] is not None and board[i][size-i-1] == piece_type
            for i in range(size)
        ): return True

        return False