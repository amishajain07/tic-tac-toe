from Schemas.PieceType import PieceType
from Models.PlayingPieces import Pieces

class PieceO(Pieces):
    def __init__(self):
        super().__init__(PieceType.O)