import chess
from typing import List, Tuple
from Player import Player


class Game:
    """
    Classe du jeu. Gère les pions, les joueurs et l'issue de la partie.
    """

    def __init__(self, board):
        # Liste des pièces au cimetière
        self.graveyard: List[chess.Piece] = []
        self.board: chess.Board = board
        self.isTurnBlack = False

    def start(self):
        player1 = Player("Andrew", False, False)
        player2 = Player("Calvin", True, False)

        while not self.board.is_checkmate():

            print(self.board)

            if self.isTurnBlack:
                move = player1.get_move(self.get_legal_move(player1.color), self.board)
                self.move_piece(move)
                self.isTurnBlack = False
            else:
                move = player2.get_move(self.get_legal_move(player2.color), self.board)
                self.move_piece(move)
                self.isTurnBlack = True

    def get_legal_move(self, color: bool) -> List[chess.Move]:
        """

        :param color: False = Noir, True = Blanc
        :return:
        """
        res = []
        for move in self.board.legal_moves:
            if self.board.color_at(move.from_square) == color:
                res.append(move)
        return res

    def move_piece(self, move: str):
        """
        Effectue un coup et l'ajoute à la pile des coups
        """
        self.board.push_uci(move)

    def revert_last_move(self):
        """
        Annule le dernier coup et reviens à la position précédente
        """
        self.board.pop()

    def eval_position(self) -> Tuple[int, int]:
        """
        Fonction qui évalue la position des deux joueurs.
        Renvoie deux int allant de 0 à 100 indiquant respectivement si le joueur est dans une mauvaise ou une bonne
        position.
        :return: int, int
        """
        pass
