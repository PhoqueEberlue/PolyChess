import chess
from typing import List


class Game:
    """
    Classe du jeu. Gère les pions, les joueurs et l'issue de la partie.
    """
    def __init__(self):
        # Liste des pièces au cimetière
        self.graveyard: List[chess.Piece] = []
