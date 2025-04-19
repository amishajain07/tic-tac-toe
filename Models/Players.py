from Models.PlayingPieces import Pieces

class Players:
    def __init__(self, user: str, playing_piece: Pieces):
        self.user = user
        self.playing_piece = playing_piece

    def get_name(self):
        return self.user
    
    def set_name(self, username:str):
        self.user = username

    def get_playing_piece(self):
        return self.playing_piece
    
    def set_playing_piece(self, playing_piece: Pieces):
        self.playing_piece = playing_piece