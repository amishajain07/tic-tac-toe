from Schemas.PieceType import PieceType
from Models.PlayingPieces import Pieces

class PieceX(Pieces):
    def __init__(self):
        super().__init__(PieceType.X)